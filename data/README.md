## Description of Files

* `anon_full_act_annotation.txt`: A text document containing the participant ID, the experimental group, and the user and system **acts** for each dialog turn in the form of semantic frames. Each frame includes the user intention, relevant slot/values, and the original user utterance.
  * Experimental groups include: `ImsExams` the passive voice chatbot variant, `ImsExams_ESThinkJ_` the direct/matter of fact chatbot variant, and `ImsExams_ESFeelJ_` the empathetic chatbot variant
* `anon_full_survey.txt`: A document including each of the Likert and free response answers from participants, user ids match those for the act annotation and transcript
* `processed_survey.csv`: A csv document with processed results (all items from a questionnaire were processed according to the questionnaire protocol), where each questionnaire is represented by a single value rather than one value for each item on the questionnaire
* `anon_full_transcript.txt`: containing the participant ID, the experimental group, and the user and system **utterances** for each dialog turn