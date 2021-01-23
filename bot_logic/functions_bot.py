import con_variables
import user, important_message, yt_vid, quote
import variables as var
import glob


def right_channel(channel):
    return channel in bot_logic.con_variables.allowed_channels


def get_command_from_content(text):

    new_text = ''

    for letter in text:
        if letter == ' ' or letter == '\n':
            break
        new_text += letter
    return new_text[1:len(new_text)]


def get_parameter_list(text, message):
    parameter_list = [message]

    if ' ' in text or '\n' in text:
        parameters = cut_parameters_from_command(text)
        parameter_list += cut_decisions(parameters)

    return parameter_list


def cut_parameters_from_command(text):
    new_text = ''
    for index in range(len(text)):
        if text[index] == ' ' or text[index] == '\n':
            new_text = text[index + 1:len(text)]
            break
    return new_text


def fill_parameters_in_list(parameters):
    parameter = ''
    parameter_list = []
    print(parameters)
    for letter in parameters:
        if letter == ' ':
            parameter_list.append(parameter)
            parameter = ''
        else:
            parameter += letter
    parameter_list.append(parameter)
    return parameter_list


def check_if_user_register(name, list):
    user_exist = False
    for member in list:
        if name == member.name:
            user_exist = True
            break

    return user_exist


def create_user(author):
    return user.User(author.id, str(author), author.mention)


def convert_dict_in_obj_list(list_obj, type_obj):

    new_list = []

    if type_obj == 'user':
        for obj in list_obj:
            new_list.append(user.User(obj['id'], obj['name'], obj['msg_cursor']))

    if type_obj == 'important_message':
        for obj in list_obj:
            new_list.append(important_message.ImportantMessage(obj['message'], obj['channel'], obj['user']))

    if type_obj == 'yt_vid':
        for obj in list_obj:
            new_list.append(yt_vid.Video(obj['link'], obj['name']))

    if type_obj == 'quote':
        for obj in list_obj:
            new_list.append(quote.Quote(obj['creator'], obj['quote']))

    return new_list


def check_link(link, yt_link):
    for i in range(len(yt_link)):
        if link[i] != yt_link[i]:
            return False
    return True


def name_of_obj_already_exist(name, obj_list):
    for obj in obj_list:
        if obj.name == name:
            return True
    return False


def cut_decisions(decisions):
    if not len(decisions):
        return 'No decisions'

    decision = ''
    decision_list = []
    string_with_whitespace = False
    for index in range(len(decisions)):
        if decisions[index] == '"' and not string_with_whitespace:
            string_with_whitespace = True
            continue

        if decisions[index] == '"' and string_with_whitespace:
            string_with_whitespace = False
            decision_list.append(decision)
            decision = ''
            continue

        if decisions[index] == ' ' and not string_with_whitespace and len(decision):
            decision_list.append(decision)
            decision = ''

        elif decisions[index] == ' ' and not string_with_whitespace:
            continue

        else:
            decision += decisions[index]

    if len(decision):
        decision_list.append(decision)

    return decision_list

#MSG functions


def get_user(id):
    for obj in var.users:
        if id == obj.id:
            return obj
    return 'ERROR'


def get_cursor_target(current_user):
    if len(current_user.msg_cursor):
        return current_user.msg_cursor.split('/')
    return ''


def get_cursor(cursor_target):
    cursor = var.msgs
    for cursor_cat in cursor_target:
        if cursor == var.msgs:
            cursor = var.msgs[cursor_cat]
        else:
            cursor = cursor[cursor_cat]
    return cursor


def info_msg_dir(current_user):
    return f'Your position {current_user.msg_cursor}\n' \
           f'```' \
           f'{var.msgs}' \
           f'```'


def create_category(cat, current_user):
    cursor_target = get_cursor_target(current_user)
    cursor = get_cursor(cursor_target)

    if cat in cursor:
        return f'Der Name der Kategorie existiert bereits!\n' \
               f'```{cat} : {cursor[cat]}```'

    cursor[cat] = {}
    return 'Kategorie wurde erfolgreich erstellt!'


def delete_category(cat, current_user):
    cursor_target = get_cursor_target(current_user)
    cursor = get_cursor(cursor_target)

    if cat in cursor:

        if type(cursor[cat]) == str:
            return "Du kannst keinen Text mit dem 'del cat' Befehl löschen"

        cursor.pop(cat)
        return 'Kategorie wurde erfolgreich gelöscht'

    return 'Something went wrong'


def create_msg(title, txt, current_user):
    cursor_target = get_cursor_target(current_user)
    cursor = get_cursor(cursor_target)

    if title in cursor:
        return f'Der Name der Kategorie existiert bereits!\n' \
               f'```{title} : {cursor[title]}```'

    cursor[title] = txt
    return 'Text wurde erfolgreich erstellt und hinzugefügt!'


def delete_msg(title, current_user):
    cursor_target = get_cursor_target(current_user)
    cursor = get_cursor(cursor_target)

    if title in cursor:

        if type(cursor[title]) == dict:
            return "Du kannst keine Ordner mit dem 'del msg' Befehl löschen"

        cursor.pop(title)
        return 'Text wurde erfolgreich gelöscht'
    return 'Something went wrong'


def set_user_cursor(next_cat, current_user):

    if next_cat == '..':
        current_user.msg_cursor_back()
        return f'Your position: {current_user.msg_cursor}'

    cursor_target = get_cursor_target(current_user)
    cursor = get_cursor(cursor_target)

    if next_cat in cursor:
        current_user.msg_cursor_next(next_cat)
        return f'Your position: {current_user.msg_cursor}'
    else:
        return f'{next_cat} wurde nicht gefunden!'


def get_note(title, current_user):
    cursor_target = get_cursor_target(current_user)
    cursor = get_cursor(cursor_target)

    if title in cursor:
        return f'```' \
               f'Title: {title}\n' \
               f'Note: {cursor[title]}' \
               f'```'

    return 'Notiz wurde nicht gefunden!'


def get_titles(current_user):
    cursor_target = get_cursor_target(current_user)
    cursor = get_cursor(cursor_target)

    titles = [title for title in cursor if type(cursor[title]) == str]

    if not len(titles):
        return 'Keine Notizen hier!'

    return '\n'.join(titles)


def set_cursor_to_begin():
    [current_user.set_cursor_to_start() for current_user in var.users]


def get_images(path):
    list_of_pics = glob.glob(path + '*.jpg')
    list_of_pics += glob.glob(path + '*.png')
    return list_of_pics



