import firebase_admin, sys, os
from firebase_admin import credentials, db

sys.path.append("D:/Cthings/prog/Bot-Python/bot_suite/tools")
import helpers as help
import constants as const

def connect_db():
    certificate_path = os.path.dirname(__file__) + "/firebase_con/bot-discord-cezario-firebase-adminsdk-tgigi-a8e006d36b.json"
    cred = credentials.Certificate(certificate_path)
    default_app = firebase_admin.initialize_app(cred,
    {'databaseURL':'https://bot-discord-cezario-default-rtdb.firebaseio.com/'})

def check_command(command : str) -> True:
    ref = db.reference("/Commands")
    commands = ref.order_by_key().get()
    if command in commands:
        return True
    return False

def insert_command(command : str, duration)-> bool:
    if check_command(command):
        return False
    ref = db.reference("/Commands")
    import json
    insert_path = os.path.dirname(__file__) + "insert_command.json"
    f = open(insert_path, "w")
    new_command = help.create_command_json(command, duration)
    f.write(new_command)
    f.close()

    try:
        with open(insert_path, "r") as f:
            file_contents = json.load(f)
        ref.update(file_contents)

    except:
        return False

    finally:
        os.remove(insert_path)
        return True

def delete_command(command : str) ->bool:
    if not check_command(command):
        return False

    try:
        ref = db.reference("/Commands")
        ref.child(command).delete()
        return True

    except Exception as e:
        print(e)
        return False

def get_command(command : str):
    ref = db.reference("/Commands")
    fire_response = ref.child(command).get()
    if fire_response == None:
        return -2
    duration =fire_response['Duration']
    if help.isfloat(duration):
        return duration
    return -1

def get_command_tuple(command : str, ref : firebase_admin.db) -> tuple:
    return [command, ref.child(command).get()['Duration']]

def get_commands() -> list:
    ref = db.reference("/Commands")
    fire_commands = ref.order_by_key().get()
    return [get_command_tuple(command, ref) for command in fire_commands if command]

