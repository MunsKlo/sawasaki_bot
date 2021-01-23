import random
import requests
import variables as var
import InputOutputJSON
import user, important_message, yt_vid, chuck_norris, quote
import functions_bot


def get_inspiro_pic(parameters):
    link = "http://inspirobot.me/api?generate=true"
    f = requests.get(link)
    imgurl = f.text
    return imgurl


def get_random_number(parameters):
    try:
        return str(random.randint(1, int(parameters[1])))
    except:
        return 'Something went wrong!'


def get_test(parameters):
    return "Test war erfolgreich!"


def get_yes_or_no(parameters):
    return f"{parameters[0].author.mention} {random.choice(['Ja', 'Nein'])}"


def get_all_members(parameters):
    for member in parameters[0].guild.members:
        print(member)
    return ''


def make_important_message(parameters):
    if len(parameters) < 2:
        return "Something went wrong"

    if parameters[1] == 'clear' and len(parameters) == 2:
        var.important_messages = []
        InputOutputJSON.write_json_file([], var.important_messages_file, True)
        return 'Alle wichtigen Nachrichten wurden gelöscht'

    elif parameters[1] == 'print' and len(parameters) == 2:
        text = ''
        for obj in var.important_messages:
            text += f'{obj.user} schrieb: "{str(obj.message)}" in {obj.channel}\n'
        if text == '':
            text = 'Keine Nachrichten vorhanden'
        return text

    else:
        message = parameters[0]
        var.important_messages.append(
            important_message.ImportantMessage(str(message.content)[3:len(message.content)], str(message.channel), str(message.author)))

        InputOutputJSON.write_json_file(var.important_messages, var.important_messages_file)

    return ''


def get_youtube(parameters):
    if len(parameters) == 4 and parameters[1] == 'add' and functions_bot.check_link(parameters[2], var.yt_link):

        if functions_bot.name_of_obj_already_exist(parameters[3], var.yt_vids):
            return 'The name already exist'

        var.yt_vids.append(yt_vid.Video(parameters[2], parameters[3]))
        InputOutputJSON.write_json_file(var.yt_vids, var.yt_vids_file)
        return 'Successfully added'

    if len(parameters) == 1 and len(var.yt_vids) > 0:
        video = var.yt_vids[random.randint(0, len(var.yt_vids) - 1)]
        return f'Name: {video.name}\n{video.link}'

    if len(parameters) == 2 and parameters[1] == 'list':
        names = ''
        for obj in var.yt_vids:
            names += f'{obj.name}\n'
        return names

    if len(parameters) == 2:
        for obj in var.yt_vids:
            if parameters[1] == obj.name:
                return obj.link
        return "Link not founded"

    else:
        return 'Something went wrong!'


def get_users(parameters):
    text = ''

    if len(parameters) == 1:
        for obj in var.users:
            text += obj.name + '\n'
        return text

    if parameters[1] == 'rand' and len(parameters) == 2:
        return str(var.users[random.randint(0, len(var.users) - 1)].name)

    return 'Something went wrong'


def get_commands(parameters):
    text = '```'
    for i in var.helper:
        text += f'{i} = {var.helper[i]}\n'
    return text + '```'


def get_decision(parameters):
    return f"{parameters[0].author.mention} {parameters[random.randint(1, len(parameters) - 1)]}"


def get_chuck_norris(parameters):
    response = requests.get('https://api.chucknorris.io/jokes/random')
    json_dict = response.json()
    joke = chuck_norris.ChuckNorris(json_dict['id'], json_dict['url'], json_dict['value'])
    return f'{joke.url}\n```{joke.joke}```'


def get_giphy_gif(parameters):
    try:
        payload = {'api_key': 'AbKxlHYeNnK7yB9kDrF9gUmHMV9pbVOF', 'Content-Type': 'application/json', 'tag': ''}
        json_dict = {'data': {'url': 'Something went wrong!'}}

        if parameters[1] == 'random' and len(parameters) == 2:
            response = requests.get('https://api.giphy.com/v1/gifs/random', params=payload)
            json_dict = response.json()

        if parameters[1] == 'random' and len(parameters) == 3:
            payload['tag'] = parameters[2]
            response = requests.get('https://api.giphy.com/v1/gifs/random', params=payload)
            json_dict = response.json()

        return f'{json_dict["data"]["url"]}'
    except Exception as e:
        return str(e)


def get_advice(parameters):
    response = requests.get('https://api.adviceslip.com/advice')
    json_dict = response.json()
    return f'```{json_dict["slip"]["advice"]}```'


def get_cat_pic(parameters):
    response = requests.get('https://aws.random.cat/meow')
    json_dict = response.json()
    return json_dict['file']


def get_dog_pic(parameters):
    response = requests.get('https://random.dog/woof.json')
    json_dict = response.json()
    return json_dict['url']


def get_fox_pic(parameters):
    response = requests.get('https://randomfox.ca/floof/')
    json_dict = response.json()
    return json_dict['image']


def handle_notes(parameters):
    result = ''

    if len(parameters) < 2:
        return 'There is no message or category!'

    current_user = functions_bot.get_user(parameters[0].author.id)

    if current_user == 'ERROR':
        return 'User not found'

    if parameters[1] == 'info':
        result = functions_bot.info_msg_dir(current_user)

    if parameters[1] == 'titles':
        result = functions_bot.get_titles(current_user)

    if parameters[1] == 'note':
        cat_string = functions_bot.cut_parameters_from_command(str(parameters[0].content))
        cat = functions_bot.cut_decisions(cat_string)[1:]

        result = functions_bot.get_note(cat[0], current_user)

    if parameters[1] == 'new' and parameters[2] == 'cat':
        cat_string = functions_bot.cut_parameters_from_command(str(parameters[0].content))
        cat = functions_bot.cut_decisions(cat_string)[2:]

        if len(cat) != 1:
            return 'Something went wrong'

        if '/' in cat[0]:
            return 'Keine / in Namen!'

        result = functions_bot.create_category(cat[0], current_user)

    if parameters[1] == 'del' and parameters[2] == 'cat':
        cat_string = functions_bot.cut_parameters_from_command(str(parameters[0].content))
        cat = functions_bot.cut_decisions(cat_string)[2:]

        if len(cat) != 1:
            return 'Something went wrong'

        result = functions_bot.delete_category(cat[0], current_user)

    if parameters[1] == 'new' and parameters[2] == 'msg':
        msg_string = functions_bot.cut_parameters_from_command(str(parameters[0].content))
        msg = functions_bot.cut_decisions(msg_string)[2:]

        if len(msg) != 2:
            return 'Something went wrong'

        result = functions_bot.create_msg(msg[0], msg[1], current_user)

    if parameters[1] == 'del' and parameters[2] == 'msg':
        msg_string = functions_bot.cut_parameters_from_command(str(parameters[0].content))
        msg = functions_bot.cut_decisions(msg_string)[2:]

        if len(msg) != 1:
            return 'Something went wrong'

        result = functions_bot.delete_msg(msg[0], current_user)

    if parameters[1] == 'purge':
        var.msgs = {}
        functions_bot.set_cursor_to_begin()
        return 'Alle Notizen und Kategorien wurden gesäubert!'

    if parameters[1] == 'cd':
        cat_string = functions_bot.cut_parameters_from_command(str(parameters[0].content))
        cat = functions_bot.cut_decisions(cat_string)[1:]

        if len(cat) != 1:
            return 'Something went wrong'

        result = functions_bot.set_user_cursor(cat[0], current_user)

    InputOutputJSON.write_json_file(var.msgs, var.msgs_file)
    InputOutputJSON.write_json_file(var.users, var.users_file)

    return result


def get_stalker(parameters):
    current_user = functions_bot.get_user(716737561791299654)
    if current_user == 'ERROR':
        return f"Nici, it is your time to shine!"
    return f"{current_user.mention}, it is your time to shine!"


def get_quote(parameters):
    if parameters[1] == 'add' and len(parameters) == 3:
        current_quote = quote.Quote(str(parameters[0].author), parameters[2])
        var.quotes.append(current_quote)
        InputOutputJSON.write_json_file(var.quotes, var.quotes_file)
        return "Erfolgreich hinzugefügt!"

    if parameters[1] == 'rand' and len(parameters) == 2:
        current_quote = random.choice(var.quotes)
        return f"{current_quote.creator} lehrte uns:" \
               f"```{current_quote.quote}```"

    return "Something went wrong"


def get_github(parameters):
    return 'Check me out! :Swag_dog:' \
           'https://github.com/MunsKlo/sawasaki_bot.git'


def get_waifu(parameters):
    if len(parameters) < 2:
        return "Something went wrong"

    if parameters[1] == 'raski':
        return f'Misaki Tobisawa\n' \
               f'{random.choice(var.pic_collection.r)}'

    if parameters[1] == 'munsklo' or parameters[1] == 'klo':
        return f'Klocke 4 eva\n' \
               f'{random.choice(var.pic_collection.m)}'

    return "Ask master MunsKlo for creating a instance for your waifu"
