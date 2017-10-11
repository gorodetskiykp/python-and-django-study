import requests
from get_token import VERSION

# TOKEN = '40042f656bbc68f2beb72d77dbf560ed048d16ec26a68a321f7f8f5aebcb494d8f6a352cd03896bb7f33c'
FRIENDS_LIMIT = 3  # None, чтобы вывести всех друзей (очень долго!)

params = {
    'v': VERSION,
    # 'access_token': TOKEN, # для поиска друзей токен не нужен
}


def get_friends(user_id):
    """Возвращает список id друзей

    Аргументы:
    user_id - id пользователя, список Id друзей которого нужно получить
    """

    params['user_id'] = user_id
    response = requests.get('https://api.vk.com/method/friends.get', params)
    return response.json()['response']['items'][:FRIENDS_LIMIT]


def get_user_fio(user_id):
    """Возвращает Фамилию Имя пользователя

    Аргументы:
    user_id - id пользователя, Фамилию Имя которого нужно получить
    """

    params['user_id'] = user_id
    response = requests.get('https://api.vk.com/method/users.get', params)
    response = response.json()['response'][0]
    return '{} {}'.format(response['last_name'], response['first_name'])


def print_friends_list(user_id, friends_freinds_level=False, num=0):
    """Выводит на экран нумерованый список друзей пользователя

    Аргументы:
    user_id - id пользователя
    friends_freinds_level (по умолчанию, False) - нужно ли выводить списки друзей у каждого друга
    num (по умолчанию, 0) - родительский номер в списке
    """
    for friend_num, friend_id in enumerate(get_friends(user_id), 1):
        if num:
            print(num, end='.')
        print('{}. {}'.format(friend_num, get_user_fio(friend_id)))
        if friends_freinds_level:
            print_friends_list(friend_id, num=friend_num)


def get_common_friends(user_id):
    """Возвращает список общих друзей пользователя и его друзей

    Аргументы:
    user_id - id пользователя
    """

    friends_list = get_friends(user_id)
    common_friends_set = set(friends_list)
    for friend in friends_list:
        common_friends_set = common_friends_set & set(get_friends(friend))
        if not common_friends_set:
            break
    return list(common_friends_set)


if __name__ == '__main__':
    print_friends_list(122055741, friends_freinds_level=True)
    common_friends = get_common_friends(122055741)
    if common_friends:
        print('\nСписок id общих друзей: {}'.format(common_friends))
    else:
        print('\nОбщих друзей нет.')
