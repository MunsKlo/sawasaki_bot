import discord
import os
import commandHandler.commandHandler
from bot_logic import admin_logic, functions_bot
from data import InputOutputJSON
from variables import variables as var

token = os.environ.get('token_raski')

comHandler = commandHandler.commandHandler.commandHandler

users_file = 'users.json'
important_messages_file = 'important_messages.json'


class MyClient(discord.Client):

    # LogIn
    async def on_ready(self):
        print("Ich bin eingeloggt!")

        var.path_data = str(__file__)[0:len(__file__) - 12] + 'data/'

        if not os.path.exists(var.path_data + var.users_file):
            with open(var.path_data + var.users_file, 'w'): pass

        if not os.path.exists(var.path_data + var.important_messages_file):
            with open(var.path_data + var.important_messages_file, 'w'): pass

        if not os.path.exists(var.path_data + var.yt_vids_file):
            with open(var.path_data + var.yt_vids_file, 'w'): pass

        if not os.path.exists((var.path_data + var.msgs_file)):
            with open(var.path_data + var.msgs_file, 'w'): pass

        if not os.path.exists((var.path_data + var.quotes_file)):
            with open(var.path_data + var.quotes_file, 'w'): pass

        var.important_messages = functions_bot.convert_dict_in_obj_list(InputOutputJSON.read_json_file(important_messages_file), 'important_message')
        var.users = functions_bot.convert_dict_in_obj_list(InputOutputJSON.read_json_file(users_file), 'user')
        var.yt_vids = functions_bot.convert_dict_in_obj_list(InputOutputJSON.read_json_file(var.yt_vids_file), 'yt_vid')
        var.quotes = functions_bot.convert_dict_in_obj_list(InputOutputJSON.read_json_file(var.quotes_file), 'quote')
        var.msgs = InputOutputJSON.read_json_file(var.msgs_file)

    # MessageSend
    async def on_message(self, message):
        if message.author == client.user:
            return

        if not functions_bot.check_if_user_register(str(message.author), var.users):
            var.users.append(functions_bot.create_user(message.author))
            InputOutputJSON.write_json_file(var.users, users_file)

        if message.content.startswith('.') or message.content.startswith('.@'):
            bot_message = ''
            result = ''

            command = functions_bot.get_command_from_content(message.content)
            parameter_list = functions_bot.get_parameter_list(message.content, message)
            print(parameter_list)

            if command in comHandler:
                function = comHandler[command]
                result = function(parameter_list)

            bot_message = result

            if command == 'vid' and len(parameter_list) > 1 and parameter_list[1] == 'add':
                await message.channel.purge(limit=1)

            if len(bot_message):
                await message.channel.send(bot_message)


# Client erstellt und mit dem Bot verbunden
client = MyClient()
client.run(token)
