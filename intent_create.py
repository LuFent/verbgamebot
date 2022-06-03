import json
from dialog import create_intent

with open("q.json") as json_file:
    questions = json.load(json_file)

for q,a in questions.items():
    create_intent(
        project_id="newagent-dhxx",
        display_name=q,
        training_phrases_parts=a['questions'],
        message_texts=[a['answer']]
    )

