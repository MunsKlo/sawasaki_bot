import json
import requests


def write_json_file(objs, file_name, clear=False):
    path = __file__[0:len(__file__) - 18]

    if file_name == 'msgs.json':
        json_string = json.dumps(objs)
        file = open(path + file_name, 'w')
        file.write(json_string)
        file.close()

    elif not clear:
        json_string = json.dumps([obj.__dict__ for obj in objs])
        file = open(path + file_name, 'w')
        file.write(json_string)
        file.close()

    else:
        file = open(path + file_name, 'w')
        file.write('')
        file.close()


def read_json_file(file_name):
    path = __file__[0:len(__file__)-18]
    json_data = ''

    with open(path + file_name, 'r') as file:

        file_text = file.readlines()

        if len(file_text) == 0 and file_name != 'msgs.json':
            return []
        elif len(file_text) == 0 and file_name == 'msgs.json':
            return {}

        if file_name != 'msgs.json':
            json_data = json.loads(file_text[0])
        else:
            json_data = json.loads(file_text[0])
    return json_data
