###############################################################################
#
# Copyright 2019, University of Stuttgart: Institute for Natural Language Processing (IMS)
#
# This file is part of Adviser.
# Adviser is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3.
#
# Adviser is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Adviser.  If not, see <https://www.gnu.org/licenses/>.
#
###############################################################################

"""Handcrafted (i.e. template-based) Natural Language Generation Module"""

import inspect
import os

from services.nlg.templates.templatefile import TemplateFile
from services.service import Service, PublishSubscribe
from services.nlg import HandcraftedNLG
from utils.common import Language
from utils.domain.domain import Domain
from utils.logger import DiasysLogger
from utils.sysact import SysAct, SysActionType
from typing import Dict, List
import string

class HandcraftedVariantNLG(HandcraftedNLG):
    """Handcrafted (i.e. template-based) Natural Language Generation Module

    A rule-based approach on natural language generation.
    The rules have to be specified within a template file using the ADVISER NLG syntax.
    Python methods that are called within a template file must be specified in the
    HandcraftedNLG class by using the prefix "_template_". For example, the method
    "_template_genitive_s" can be accessed in the template file via calling {genitive_s(name)}

    Attributes:
        domain (Domain): the domain
        template_filename (str): the NLG template filename
        templates (TemplateFile): the parsed and ready-to-go NLG template file
        template_english (str): the name of the English NLG template file
        template_german (str): the name of the German NLG template file
        language (Language): the language of the dialogue
    """
    def __init__(self, domain: Domain, base_name: str, variations: List[str], logger: DiasysLogger = DiasysLogger(), sub_topic_domains: Dict[str, str] = {}):
        """Constructor mainly extracts methods and rules from the template file"""
        Service.__init__(self, domain=domain, sub_topic_domains=sub_topic_domains)

        self.domain = domain
        self.user_assignments = {}  # this is tracked at a module level so we can balance these groups out
        self.logger = logger
        self.templates = {}

        self.initialize_templates(base_name, variations)

    @PublishSubscribe(sub_topics=["sys_act"], pub_topics=["sys_utterance"])
    def generate_system_utterance(self, user_id: str = "default", sys_act: SysAct = None) -> dict(sys_utterance=str):
        """

        Takes a system act, searches for a fitting rule, applies it
        and returns the message.

        Args:
            sys_act (SysAct): The system act, to check whether the dialogue was finished

        Returns:
            dict: a dict containing the system utterance
        """
        # message = str(sys_acts)
        rule_found = True
        message = ""
        bad_act = None

        template = self.templates[self.get_template(user_id)]

        try:
            message = template.create_message(sys_act)
        except BaseException as error:
            rule_found = False
            self.logger.error(error)
            bad_act = sys_act
            # raise(error)

        # inform if no applicable rule could be found in the template file
        if not rule_found:
            self.logger.info(f'# USER {user_id} # NLG-ERROR ({self.domain.get_domain_name()}) - Could not find a fitting rule for the given system act!')
            self.logger.info(f"# USER {user_id} # NLG-ERROR ({self.domain.get_domain_name()}) - System Action: {str(bad_act.type)} - Slots: {str(bad_act.slot_values)}")

        self.logger.dialog_turn(f"# USER {user_id} # NLG-MSG ({self.domain.get_domain_name()}) - {message}")
        return {'sys_utterance': message}


    def initialize_templates(self, base_name: str, variations: List[str]):
        """
            load in the templates for the base and each variation storing them in a list: [base, var1, var2, ..., varN]
        """
        names = [base_name] + [base_name + variation for variation in variations]
        for f_name in names:
            self.user_assignments[f_name] = set()
            template_filename = os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                '../../resources/nlg_templates/%sMessages.nlg' % f_name)
            template = TemplateFile(template_filename, self.domain)
            self._add_additional_methods_for_template_file(template)
            self.templates[f_name] = template

    def _add_additional_methods_for_template_file(self, template):
        """add the function prefixed by "_template_" to the template file interpreter"""
        for (method_name, method) in inspect.getmembers(type(self), inspect.isfunction):
            if method_name.startswith('_template_'):
                template.add_python_function(method_name[10:], method, [self])

    def get_template(self, user_id: str):
        """
            args:
                user_id (str): identifier for the current user

            returns:
                the name (key) of the template associated with the user, if there is not yet one,
                assigns to the next available group
        """
        base_distro = {'ImsExams': 24, "ImsExams_ESFeelJ_": 28, "ImsExams_ESThinkJ_": 25}
        # lookup which category a user is in
        cat_lengths = []
        for category in self.user_assignments:
            if user_id in self.user_assignments[category]:
                return category
            cat_lengths.append((category, len(self.user_assignments[category]) + base_distro[category]))
        
        # get category with least number of members
        cat_lengths.sort(key=lambda x: x[1])
        next_cat = cat_lengths[0][0]

        # add user and log their assignment
        self.user_assignments[next_cat].add(user_id)
        self.logger.info(f'# USER {user_id} # CONDITION: {next_cat}')

        return next_cat

        
