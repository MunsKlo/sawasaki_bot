important_messages = []

users = []

yt_vids = []

users_file = 'users.json'
important_messages_file = 'important_messages.json'
yt_vids_file = 'yt_vids.json'
msgs_file = 'msgs.json'
quotes_file = "quotes.json"

#CheckStates
path_data = ''

yt_link = 'https://www.youtube.com/watch?'

helper = {
    ".help": "Get all commands",
    "Fun":'',
    ".vid": "Get a random video",
    ".vid add <link> <name>": "Add a video with a name",
    ".vid list": "List all names of videos",
    ".vid <name>": "Get a video with a name",
    ".inspiro": "Get a random picture from the inspiro-bot",
    ".giphy random": "Give you a absolute random gif",
    ".giphy random <tag>": "Give you a random gif from a specific topic",
    ".chucknorris": "Get a Chuck Norris joke",
    ".cat": "Give you a random cat picture",
    ".dog": "Give you a random dog picture",
    ".fox": "Give you a random fox picture",
    ".stalk": "Nici incoming!",
    "Helpful": '',
    ".jn <question>": "Get a yes or no answer to a question",
    ".number <number>": "Get a random number ",
    ".test": "Test the bot",
    ".advice": "Give you a random advice",
    ".decision <decision1> <decision2> <decision n>": "Take randomly a decision",
    "Important": "",
    ".members": "Coming soon",
    ".users": "Get a list of all users",
    ".users rand": "Get an user randomly",
    ".@": "Create a important message",
    ".@ clear": "Delete all important messages",
    "note-system": "",
    ".msg info": "Give you your current position and the note-system",
    ".msg note <title": "Give you the content of the note",
    ".msg titles": "Give you all the titles from your currently position",
    ".msg new msg <title> <note>": "Create a new note in the note-system",
    ".msg new cat <title>": "Create a new category in the note-system",
    ".msg del msg <title>": "Remove the note from the note-system",
    ".msg del cat <title>": "Remove the category from the note-system",
    "IMPORTANT": '',
    ".msg purge": "DELETE ALL THE CONTENT IN THE NOTE-SYSTEM",

}

msgs = {}

quotes = []
