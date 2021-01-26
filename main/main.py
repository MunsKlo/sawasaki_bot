import discord
import os, sys

path = str(__file__)[0:len(__file__) - 12]

sys.path.append(f'{path}commandHandler\\')
sys.path.append(f'{path}bot_logic\\')
sys.path.append(f'{path}data\\')
sys.path.append(f'{path}variables\\')
sys.path.append(f'{path}model\\')

import commandHandler
import admin_logic, functions_bot
import InputOutputJSON
import variables as var
import pic_collections

token = os.environ.get('token_raski')

comHandler = commandHandler.commandHandler

path = str(__file__)[0:len(__file__) - 12]

var.pic_collection = pic_collections.PicCollection()

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

        var.important_messages = functions_bot.convert_dict_in_obj_list(InputOutputJSON.read_json_file(var.important_messages_file), 'important_message')
        var.users = functions_bot.convert_dict_in_obj_list(InputOutputJSON.read_json_file(var.users_file), 'user')
        var.yt_vids = functions_bot.convert_dict_in_obj_list(InputOutputJSON.read_json_file(var.yt_vids_file), 'yt_vid')
        var.quotes = functions_bot.convert_dict_in_obj_list(InputOutputJSON.read_json_file(var.quotes_file), 'quote')
        var.msgs = InputOutputJSON.read_json_file(var.msgs_file)

        var.pic_collection.r = functions_bot.get_images(f'{path}/pictures/picCollection_w/r/')
        var.pic_collection.m = functions_bot.get_images(f'{path}/pictures/picCollection_w/m/')
        var.pic_collection.y = functions_bot.get_images(f'{path}/pictures/picCollection_w/y/')
        var.pic_collection.l = functions_bot.get_images(f'{path}/pictures/picCollection_w/l/')
        var.pic_collection.f = functions_bot.get_images(f'{path}/pictures/picCollection_w/f/')

    # MessageSend
    async def on_message(self, message):
        if message.author == client.user:
            return

        if not functions_bot.check_if_user_register(str(message.author), var.users):
            var.users.append(functions_bot.create_new_user(message.author))
            InputOutputJSON.write_json_file(var.users, var.users_file)

        if message.content.startswith('.') or message.content.startswith('.@'):
            bot_message = ''
            result = ''

            command = functions_bot.get_command_from_content(message.content)
            parameter_list = functions_bot.get_parameter_list(message.content, message)
            print(parameter_list)

            command = str(command).lower()

            if command in comHandler:
                function = comHandler[command]
                result = function(parameter_list)

            bot_message = result

            if command == 'vid' and len(parameter_list) > 1 and parameter_list[1] == 'add':
                await message.channel.purge(limit=1)

            if len(bot_message) and '\n' in bot_message and command=='waifu':
                bot_messages = bot_message.split('\n')
                await message.channel.send(bot_messages[0])
                await message.channel.send(file=discord.File(bot_messages[1]))

            elif len(bot_message):
                await message.channel.send(bot_message)


# Client erstellt und mit dem Bot verbunden
client = MyClient()
client.run(token)
