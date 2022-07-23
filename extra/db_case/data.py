import firebase_admin, sys, os
from firebase_admin import credentials, db
import json

certificate_path = "D:/Cthings/prog/Bot-Python/bot_suite/tools/firebase_con/bot-discord-cezario-firebase-adminsdk-tgigi-a8e006d36b.json"
cred = credentials.Certificate(certificate_path)
default_app = firebase_admin.initialize_app(cred,
{'databaseURL' : 'https://bot-discord-cezario-default-rtdb.firebaseio.com/'})

ref = db.reference("/Commands")
insert_path = "D:/Cthings/prog/Bot-Python/bot_suite/tools/db_case/commands.json"
with open(insert_path, "r") as f:
    file_contents = json.load(f)
ref.set(file_contents)