import json
from dialog import create_intent
import logging
import os
from dotenv import load_dotenv


load_dotenv()
project_id=os.environ['DIALOG_FLOW_ID']

with open("intents.json") as intents:
    intents = json.load(intents)

for tittle, questions_and_replies in intents.items():
    create_intent(
        project_id=project_id,
        display_name=tittle,
        training_phrases_parts=questions_and_replies['questions'],
        message_texts=[questions_and_replies['answer']]
    )

