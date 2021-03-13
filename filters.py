


def recognize_name(first_name, last_name, username, chat_id):
    if first_name != 'None' and last_name != 'None':
        name = first_name + ' ' + last_name
    elif first_name != 'None' and last_name == 'None':
        name = first_name
    elif first_name == 'None' and last_name != 'None':
        name = last_name
    elif first_name == 'None' and last_name == 'None' and username == 'None':
        name = str(' человек под номером: {} '.format(chat_id))
    else:
        name = username
    return name