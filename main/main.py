import discord, asyncio
import os, sys
from commandHandler import commandHandler
from bot_logic import admin_logic, functions_bot
from data import InputOutputJSON
from variables import variables as var
from model import pic_collections, riddle, user
from discord.ext import commands

path = str(__file__)[0:len(__file__) - 12]

#sys.path.append(f'{path}commandHandler\\')
#sys.path.append(f'{path}bot_logic\\')
#sys.path.append(f'{path}data\\')
#sys.path.append(f'{path}variables\\')
#sys.path.append(f'{path}model\\')


token = os.environ.get('token_raski')

comHandler = commandHandler.commandHandler

var.pic_collection = pic_collections.PicCollection()

current_riddle = riddle.Riddle()


class MyClient(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        #self.bg_inspiro = self.loop.create_task(self.create_inspiro())
        self.bg_riddle_make = self.loop.create_task(self.make_riddle())
        self.bg_riddle = self.loop.create_task(self.create_riddle())


    # LogIn
    async def on_ready(self):
        print("Ich bin eingeloggt!")
        #await client.change_presence(activity=discord.Game(name='Bullet Girls 2'))
        activity = discord.Activity(name='sich Nicis Zuhause an', type=discord.ActivityType.watching)
        await client.change_presence(activity=activity)

        var.path = str(__file__)[0:len(__file__) - 12]
        var.path_data = var.path + 'data/'

        if not os.path.exists(var.path_data + var.yt_vids_file):
            with open(var.path_data + var.yt_vids_file, 'w'): pass

        if not os.path.exists((var.path_data + var.msgs_file)):
            with open(var.path_data + var.msgs_file, 'w'): pass

        if not os.path.exists((var.path_data + var.quotes_file)):
            with open(var.path_data + var.quotes_file, 'w'): pass

        var.yt_vids = functions_bot.convert_dict_in_obj_list(InputOutputJSON.read_json_file(var.yt_vids_file), 'yt_vid')
        var.quotes = functions_bot.convert_dict_in_obj_list(InputOutputJSON.read_json_file(var.quotes_file), 'quote')
        var.msgs = InputOutputJSON.read_json_file(var.msgs_file)

        var.pic_collection.r = functions_bot.get_images(f'{path}/pictures/picCollection_w/r/')
        var.pic_collection.m = functions_bot.get_images(f'{path}/pictures/picCollection_w/m/')
        var.pic_collection.y = functions_bot.get_images(f'{path}/pictures/picCollection_w/y/')
        var.pic_collection.l = functions_bot.get_images(f'{path}/pictures/picCollection_w/l/')
        var.pic_collection.lha = functions_bot.get_images(f'{path}/pictures/picCollection_w/lh/a/')
        var.pic_collection.lhb = functions_bot.get_images(f'{path}/pictures/picCollection_w/lh/b/')
        var.pic_collection.f = functions_bot.get_images(f'{path}/pictures/picCollection_w/f/')
        var.pic_collection.k = functions_bot.get_images(f'{path}/pictures/picCollection_w/k/')
        var.pic_collection.n = functions_bot.get_images(f'{path}/pictures/picCollection_w/n/')

        for member in client.guilds[1].members:
            var.users.append(user.User(member))

        functions_bot.load_points()
        functions_bot.get_riddles(var.riddleList)

    # MessageSend
    async def on_message(self, message):
        if message.author == client.user:
            return

        if 'vodka' in message.content.lower() or 'wodka' in message.content.lower():
            emoji = functions_bot.get_emoji(client.guilds[1].emojis, 'Wodka')
            await message.add_reaction(emoji)

        if message.content.startswith('.') or message.content.startswith('.@'):
            bot_message = ''
            result = ''

            commando = functions_bot.get_command_from_content(message.content)
            parameter_list = functions_bot.get_parameter_list(message.content, message)
            print(parameter_list)

            commando = str(commando).lower()

            if commando == 'help':
                await message.author.send(comHandler[commando](parameter_list))

            elif commando in comHandler:
                function = comHandler[commando]
                result = function(parameter_list)

            bot_message = result

            if commando == 'vid' and len(parameter_list) > 1 and parameter_list[1] == 'add':
                await message.channel.purge(limit=1)

            if commando == 'waifu' or commando == 'husbando' and '\n' in bot_message:
                    bot_messages = bot_message.split('\n')
                    await message.channel.send(bot_messages[0])
                    await message.channel.send(file=discord.File(bot_messages[1]))

            elif commando == 'gif' and parameter_list[1] not in bot_message:
                await message.channel.send(bot_message)

            elif len(bot_message):
                await message.channel.send(bot_message)

    async def on_message_delete(self, message):
        if message.author == client.user:
            return

        await message.channel.send(f'{message.author} löschte: {message.content}')

    async def on_member_join(self, member):
        channel = functions_bot.get_channel(client.guilds[1].channels, 'neuzugang')
        channel.send(f'Willkommen {member.mention}')

    async def create_inspiro(self):
        await self.wait_until_ready()
        meme_channel = functions_bot.get_channel(client.guilds[1].channels, 'meme')
        while not self.is_closed():
            await meme_channel.send(comHandler['inspiro']())
            await asyncio.sleep(14400)

    async def create_riddle(self):
        await self.wait_until_ready()
        riddle_channel = functions_bot.get_channel(client.guilds[0].channels, 'commandbot')
        while not self.is_closed():
            global current_riddle
            question = current_riddle.question
            await  riddle_channel.send(question)
            await asyncio.sleep(30)

    async def make_riddle(self):
        await self.wait_until_ready()
        while not self.is_closed():
            global current_riddle
            current_riddle = await functions_bot.get_riddle()
            await asyncio.sleep(30)


# Client erstellt und mit dem Bot verbunden
client = MyClient()
client.run(token)
