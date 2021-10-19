import datetime
from datetime import timedelta, datetime
from passlib.context import CryptContext
import jwt
import tornado.ioloop
import tornado.web
from tornado.websocket import WebSocketHandler
import json
import pymysql
import os

from services.service import PublishSubscribe, Service, DialogSystem
from services.nlu import HandcraftedNLU
from services.bst import HandcraftedBST
from services.policy import HandcraftedPolicy
from services.nlg.variant_nlg import HandcraftedVariantNLG
from services.domain_tracker.domain_tracker import DomainTracker
from utils.topics import Topic
from utils.logger import DiasysLogger, LogLevel
from utils.survey_logger import SurveyLogger
from utils.domain.jsonlookupdomain import JSONLookupDomain
import time
from utils.sysact import SysActionType
from utils.useract import UserActionType
from utils.beliefstate import BeliefState
import random
from typing import List
import copy

# to get a string like this run: openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 180
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

logger = DiasysLogger(name="userlog", console_log_lvl=LogLevel.NONE, file_log_lvl=LogLevel.DIALOGS)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str):
    return pwd_context.hash(password)


# create db
def create_userdb():
    try:
        if not os.path.isfile("users.mysqldb"):
            connection = pymysql.connect("localhost", "dbowner2", "abcd1234", "USERDB")
            print("DB Users not found - creating ")
            cursor = connection.cursor()
            # Tabelle erzeugen
            sql = """CREATE TABLE IF NOT EXISTS Users(
                userid VARCHAR(255) PRIMARY KEY,
                hash TEXT NOT NULL,
                disabled BOOL NOT NULL
                ); """
            cursor.execute(sql)
            connection.commit()
            cursor.close()
        else:
            print("DB Users was found - connection established")
            connection = pymysql.connect("localhost", "dbowner", "1!:xaw0?asd24", "USERDB")

        return connection
    except:
        import traceback
        print(traceback.format_exc())
        print("SQLERROR: Could not connect to database / create table failed")

dbconn = create_userdb()

# def insert_user(dbconn: sqlite3.Connection, userid: str, pwd_plaintext: str):
#     try:
#         cursor = dbconn.cursor()
#         cursor.execute("INSERT INTO Users(userid, hash, disabled) VALUES(?,?,?)", 
#                              (userid, get_password_hash(pwd_plaintext), False))
#         dbconn.commit()
#         return True
#     except:
#         print("SQLERROR: Failed to create user:", userid)
#         import traceback
#         import sys
#         traceback.print_exc(file=sys.stdout)
#     return False


# try:
#     print("Creating testuser")
#     insert_user(dbconn, "abcd", "abcd")
# except:
#     print("Testuser exists already")

# class User():
#     def __init__(self, userid, hashed_password, disabled):
#         super().__init__()
#         self.userid = userid
#         self.hashed_password = hashed_password
#         self.disabled = disabled


# def authenticate_user(conn, userid: str, password: str):
#     user = get_user(conn, userid)
#     if not user:
#         print(f"ACCESS WARNING: user '{userid}' not in DB")
#         return False
#     if not verify_password(password, user.hashed_password):
#         print(f"ACCESS WARNING: wrong password for user '{userid}'")
#         return False
#     return user


def insert_user(dbconn, userid: str):
    try:
        cursor = dbconn.cursor()
        cursor.execute(f"INSERT INTO Users(userid, hash, disabled) VALUES(%s,%s,FALSE)", (userid, "None"))
        dbconn.commit()
        return True
    except:
        print("SQLERROR: Failed to create user:", userid)
        import traceback
        import sys
        traceback.print_exc(file=sys.stdout)
    return False


def gen_key(dbconn, userid):
    """
        generates a random 7 digit key for users on completion of task, check first that it is not already in the database
    """
    character_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    unique = False
    while not unique:
        generated_key = ''.join(random.choices(population=character_set, k=7))
        try:
            cursor = dbconn.cursor()
            cursor.execute(f"SELECT hash FROM Users")
            results = cursor.fetchall()
            results = set([r[0] for r in results])
            if generated_key not in results:
                unique = True
        except:
            print("SQLERROR: Failed to update information for user: ", userid)
            import traceback
            import sys
            traceback.print_exc(file=sys.stdout) 
            unique = True
    return generated_key         



def update_user_hash(dbconn, userid: str):
    """
        updates the hash value in the database with a randomly generated key after user completes experiment
    """
    cursor = dbconn.cursor()
    cursor.execute("SELECT * FROM Users WHERE userid=%s", (userid,))
    result = cursor.fetchone()
    if result[1] != "None":
        return result[1]
    key = gen_key(dbconn=dbconn, userid=userid)
    if key:
        try:
            cursor.execute(f"REPLACE INTO Users(userid, hash, disabled) VALUES(%s,%s,FALSE)", (userid, key))
            dbconn.commit()
            return key
        except:
            print("SQLERROR: Failed to update information for user: ", userid)
            import traceback
            import sys
            traceback.print_exc(file=sys.stdout)


def get_user(conn, userid: str):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Users WHERE userid=%s", (userid,))
        result = cursor.fetchone()
        if result:
            return User(userid=userid, hashed_password=result[1], disabled=result[2])
    except:
        pass
    finally:
        cursor.close()
    return None


class User():
    def __init__(self, userid, verification_hash, disabled):
        super().__init__()
        self.userid = userid
        self.verification_hash = verification_hash
        self.disabled = disabled


def get_user(conn, userid: str):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Users WHERE userid=%s", (userid,))
        result = cursor.fetchone()
        if result:
            return User(userid=userid, verification_hash=result[1], disabled=result[2])
    except:
        pass
    finally:
        cursor.close()
    return None


def authenticate_user(conn, userid: str):
    user = get_user(conn, userid)
    if not user:
        insert_user(dbconn=conn, userid=userid)
        print(f"ADDING USER: {userid}")
        user = get_user(conn, userid)
    elif user.verification_hash != 'None':
        print(f"ACCESS WARNING: '{userid}' has already completed the experiment")
        return False
    return user    

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=60)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt.decode("utf-8")

def user_from_token(token):
    """ Extract userid from token, if token is still valid.
    If user is registered + token is not expired, returns userid
    else, return None
    """
    try:
        # automatically checks expired property
        jwt_payload = jwt.decode(token, SECRET_KEY, verify=True, algorithm=ALGORITHM)
        if 'userid' in jwt_payload:
            return jwt_payload['userid']
    except:
        pass
    return None


class CorsJsonHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        # allow requests from anywhere (CORS)
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with,access-control-allow-origin,authorization,content-type")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def options(self):
        # no body
        self.set_status(204)
        self.finish()
    
    def prepare(self):
        # extract json
        if self.request.headers.get("Content-Type", "").startswith("application/json"):
            self.json_args = json.loads(self.request.body)
        else:
            self.json_args = None


class LoginHandler(CorsJsonHandler):
    def post(self):
        if self.json_args:
            userid = self.json_args['userid']
            # pwd_plaintext = self.json_args['pwd']
            user = authenticate_user(dbconn, userid)
            if user:
                logger.dialog_turn(f"USER {userid} LOGGED IN")
                access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
                access_token = create_access_token(data={"userid": userid}, expires_delta=access_token_expires)
                self.write({"access_token": access_token})
                self.set_status(200)
            else:
                logger.dialog_turn("FAILED LOGIN ATTEMPT")
                self.set_status(401, reason="Unauthorized")
        else:
            self.set_status(402, reason="Expected JSON")
        self.finish()

class RegisterHandler(CorsJsonHandler):
    def post(self):
        if self.json_args:
            userid = self.json_args['userid']
            pwd_plaintext = self.json_args['pwd']

            print("registering user", userid)
            if get_user(dbconn, userid):
                print(f"user {userid} already exists")
                self.set_status(401, reason="User already exists")
            else:
                if not insert_user(dbconn, userid=userid, pwd_plaintext=pwd_plaintext):
                    self.set_status(402, reason="Error while creating new User")
        else:
            self.set_status(403, reason="Expected JSON")
        self.finish() 


import asyncio
class GUIServer(Service):
    def __init__(self, domains, logger, goals=[]):
        super().__init__(domain="", debug_logger=logger)
        self.websockets = {}
        self.domains = domains
        self.logger = logger
        self.loopy_loop = asyncio.new_event_loop()
        self.survey_logger = SurveyLogger()
        self.headers = []
        self.start_goals = goals

    def dialog_start(self, user_id: str = "default"):
        self.set_state(user_id=user_id, attribute_name="goal_state", attribute_value="default")
        self.set_state(user_id=user_id, attribute_name="num_complete_goals", attribute_value=0)
        self.set_state(user_id=user_id, attribute_name="goals", attribute_value=copy.deepcopy(self.start_goals))

    
    def log_consent(self, user_id: str = "default"):
        self.logger.dialog_turn(f"# USER {user_id} CONSENTED TO DATA AGREEMENT")

    @PublishSubscribe(pub_topics=['user_utterance'])
    def user_utterance(self, user_id = "default", domain_idx = 0, message = ""):
        try:
            self.logger.dialog_turn(f"# USER {user_id} # USR-UTTERANCE ({self.domains[domain_idx].get_domain_name()}) - {message}")
            return {f'user_utterance/{self.domains[domain_idx].get_domain_name()}': message, "user_id": user_id}
        except:
            print("ERROR in GUIService - user_utterance: user=", user_id, "domain_idx=", domain_idx, "message=", message)
            import traceback
            import sys
            traceback.print_exc(file=sys.stdout)
            return {}

    def send_survey_code(self, user_id):
        key = update_user_hash(dbconn=dbconn, userid=user_id)
        if key:
            self.logger.dialog_turn(f"# USER {user_id} # SURVEY CODE: {key}")
            self.forward_message_to_react(message=key, topic="survey_code", user_id=user_id)
     

    @PublishSubscribe(sub_topics=['sys_utterance'])
    def forward_sys_utterance(self, user_id: str, sys_utterance: str):
        if "Please rate this conversation" in sys_utterance:
            if self.get_state(user_id=user_id, attribute_name="goal_state") == "done":
                self.forward_message_to_react(message=sys_utterance, topic="sys_utterance", user_id=user_id,)
                if "Please rate this conversation" in sys_utterance:
                    self.forward_message_to_react(message="dialog_complete", topic="dialog_complete", user_id=user_id)
            else:
                self.forward_message_to_react(message="Not all goals have been met, please make sure to fulfill all the goals listed in the instructions before ending the dialog", topic="sys_utterance", user_id=user_id)
        else:
            self.forward_message_to_react(message=sys_utterance, topic="sys_utterance", user_id=user_id)
            self.forward_message_to_react(message=self.get_state(user_id=user_id, attribute_name="num_complete_goals"), topic="num_completed_goals", user_id=user_id)

    def forward_message_to_react(self, message, topic: str, user_id: str = "default"):
        asyncio.set_event_loop(self.loopy_loop)
        self.websockets[user_id].write_message({"topic": topic, "msg": message})

    def log_survey_results(self, survey_dict, user_id: str = "default"):
        """
        """
        if not self.headers:
            self.headers = ["user_id"]
            self.headers += [key for key in survey_dict if key not in ['topic', 'access_token']]
            self.survey_logger.result("|".join(self.headers))
        survey_dict["user_id"] = user_id        
        data = [survey_dict[key] for key in self.headers]
        self.survey_logger.result("|".join(data))

    @PublishSubscribe(sub_topics=['beliefstate'])
    def _update_goal_progress(self, user_id: str = "default", beliefstate: BeliefState = None):
        self.set_state(user_id=user_id, attribute_name="goal_state", attribute_value="default")
        informs_done = False
        requests_done = False

        nonprobabalistic_bs = {}
        for slot in beliefstate["informs"]:
            value = sorted(beliefstate["informs"][slot].items(), key=lambda item: item[1])[-1][0]
            nonprobabalistic_bs[slot] = value
        goals = self.get_state(user_id, "goals")

        if len(goals) == 0:
            self.set_state(user_id, "goal_state", "done")
            self.logger.dialog_turn(f"# USER {user_id} # GOAL COMPLETED")        
        else:
            # check all user acts are contributing to goal
            if len(goals[0]["informs"]) > 0:
                if nonprobabalistic_bs == goals[0]["informs"]:
                    informs_done = True
                elif not set(nonprobabalistic_bs.keys()).issubset(set(goals[0]["informs"].keys())):
                    self.set_state(user_id, "goal_state", "outside goal")
            else:
                informs_done = True
            
            bs_requests = set([slot for slot in beliefstate["requests"]])
            if bs_requests == goals[0]["requests"]:
                requests_done = True
            elif not bs_requests.issubset(goals[0]["requests"]):
                self.set_state(user_id, "goal_state", "outside goal")
        # if this goal is fulfilled, remove from list
        if informs_done and requests_done:
            goals.pop(0)
            self.set_state(user_id, "goals", goals)
            num_complete_goals = self.get_state(user_id, "num_complete_goals")
            self.set_state(user_id, "num_complete_goals", num_complete_goals + 1)

goals = []
goals.append({"informs": {"name": "requirements module"}, "requests": set()})
goals.append({"informs": {"name": "requirements module"}, "requests": set(["registration"])})
goals.append({"informs": {"name": "requirements module"}, "requests": set(["registration_withdrawal"])})
goals.append({"informs": {}, "requests": set(["registration_period_wise"])})
goals.append({"informs": {"name": "requirements module"}, "requests": set(["acceptance_belated_registration"])})
goals.append({"informs": {"name": "master thesis"}, "requests": set()})
goals.append({"informs": {"name": "master thesis"}, "requests": set(["acceptance_belated_registration"])})
goals.append({"informs": {"name": "master thesis"}, "requests": set(["registration"])})
goals.append({"informs": {"name": "master thesis"}, "requests": set(["registration_withdrawal"])})

d = JSONLookupDomain("ImsExams")
nlu = HandcraftedNLU(domain=d, logger=logger)
bst = HandcraftedBST(domain=d,logger=logger)
policy = HandcraftedPolicy(domain=d, logger=logger)
nlg = HandcraftedVariantNLG(domain=d, base_name="ImsExams", variations=["_ESFeelJ_", "_ESThinkJ_"], logger=logger)

domains = [d]
gui_service = GUIServer(domains, logger, goals)
services = [nlu, bst, policy, nlg, gui_service]
ds = DialogSystem(services=services, debug_logger=logger)
error_free = ds.is_error_free_messaging_pipeline()
if not error_free:
    ds.print_inconsistencies()
# ds.draw_system_graph()


class SimpleWebSocket(tornado.websocket.WebSocketHandler):

    def _extract_token(self, uri):
        start=len("/ws?token=")
        return uri[start:]

    def open(self, *args):
        token = self._extract_token(self.request.uri)
        userid = user_from_token(token)
        if userid:
            gui_service.websockets[userid] = self
 
    def on_message(self, message):
        data = json.loads(message)
        # check token validity
        user_id = user_from_token(data['access_token'])
        if user_id:
            topic = data['topic']
            domain_index = 0
            if topic == 'start_dialog':
                logger.dialog_turn(f"# USER {user_id} # DIALOG-START ({domains[domain_index].get_domain_name()})")
                ds._start_dialog(start_signals={f'user_utterance/{domains[domain_index].get_domain_name()}': ''}, user_id=user_id)
                logger.dialog_turn(f"SUCCESSFULLY STARTED DIALOG for USER{user_id}")
            elif topic == 'user_utterance':
                gui_service.user_utterance(user_id=user_id, domain_idx=domain_index, message=data['msg'])
            elif topic == "user_consented":
                gui_service.log_consent(user_id=user_id)
            elif topic == "get_survey_code":
                gui_service.send_survey_code(user_id=user_id)
            elif topic == "survey_results":
                gui_service.log_survey_results(user_id=user_id, survey_dict=data)
    
    def on_close(self):
        # find right connection to delete
        for userid in gui_service.websockets:
            if gui_service.websockets[userid] == self:
                logger.dialog_turn(f"# USER {userid} # SOCKET-CLOSE")
                del gui_service.websockets[userid]
                break

    def check_origin(self, *args, **kwargs):
        # allow cross-origin
        return True

def make_app():
    return tornado.web.Application([
        (r"/login", LoginHandler),
        (r"/register", RegisterHandler),
        (r"/ws", SimpleWebSocket)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(44123)
    tornado.ioloop.IOLoop.current().start()