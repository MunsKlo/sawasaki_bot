import random
import requests
from variables import variables as var
from data import InputOutputJSON
from model import user, important_message, yt_vid, chuck_norris, quote
from bot_logic import functions_bot


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

        return f'{str(parameters[0].author.mention)}:\n' \
               f'{json_dict["data"]["url"]}'
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

    parameters[1] = parameters[1].lower()

    if parameters[1] == 'raski':
        return f'Misaki Tobisawa\n' \
               f'{random.choice(var.pic_collection.r)}'

    if parameters[1] == 'munsklo' or parameters[1] == 'klo' or parameters[1] == 'muns':
        return f'Yuki Kaizuka\n' \
               f'{random.choice(var.pic_collection.k)}'

    if parameters[1] == 'klocke':
        return f'Klocke 4 eva\n' \
               f'{random.choice(var.pic_collection.m)}'

    if parameters[1] == 'yuzu':
        return f'FrostNova\n' \
               f'{random.choice(var.pic_collection.y)}'

    if parameters[1] == 'lauri' or parameters[1] == 'laurii':
        return f'RIP Teddy D:\n' \
               f'{random.choice(var.pic_collection.l)}'

    if parameters[1] == 'flocke' or parameters[1] == 'flo':
        return f'Hinata Hyuuga\n' \
               f'{random.choice(var.pic_collection.f)}'
    return "Ask master MunsKlo for creating an instance for your waifu"


def get_husbando(parameters):
    parameters[1] = parameters[1].lower()

    if parameters[1] == 'nici':
        return f'Yato\n' \
               f'{random.choice(var.pic_collection.n)}'

    if parameters[1] == 'lauri' or parameters[1] == 'laurii':
        numb = random.choice([1, 2])
        if numb == 1:
            return f'Aiji Yanagi\n' \
                   f'{random.choice(var.pic_collection.lha)}'
        return f'Souji Okita\n' \
               f'{random.choice(var.pic_collection.lhb)}'

    return "Ask master MunsKlo for creating an instance for your husbando"


def get_joke(parameters):
    country = '?lang=de'

    if len(parameters) > 1:
        parameters[1] = parameters[1].lower()
        if parameters[1] == 'en':
            country = ''
        if parameters[1] == 'fr':
            country = '?lang=fr'

    response = requests.get(f'https://v2.jokeapi.dev/joke/Any{country}')
    json_dict = response.json()
    joke = json_dict['setup']
    solution = json_dict['delivery']
    return f'{joke}\n' \
           f'||{solution}||'

def get_fact(parameters):
    response = requests.get(f'https://uselessfacts.jsph.pl/random')


