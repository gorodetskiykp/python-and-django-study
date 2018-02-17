documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def exit():
    return False
    
def show_commands():
    print(' q – выход\n',
          'h – список команд\n',
          'p – имя человека, которому принадлежит документ\n',
          'l – список всех документов\n',
          's – номер полки, на которой находится документ\n',
          'a – добавить новый документ в каталог и в перечень полок\n',
          'd – удалить документ из каталога и из перечня полок\n',
          'm – переместить документ с текущей полки на целевую\n',
          'as – добавить новую полку в перечень'
          )
    return True
          

def show_people():
    while True:
        document_id = input('Введите номер документа (q - для выхода):')
        if document_id == 'q':
            return True
        show_list(document_id)
    return True

def show_list(document_id=''):
    found_documents = []
    for document in documents:
        if document_id == '' or document_id == document['number']:
            print('{:<13}{:<20}{}'.format(
                document['type'],
                document['number'],
                document['name'],
                ))
            found_documents.append(document['number'])
    return found_documents

def show_shelf():
    while True:
        document_id = input('Введите номер документа (q - для выхода):')
        if document_id == 'q':
            return True
        for shelf, documents in directories.items():
            for document in documents:
                if document_id in document:
                    print('{:<20}{}'.format(document, shelf))
    return True

def add_document():
    document_id = input('Введите номер документа:')
    document_type = input('Введите тип документа:')
    document_owner = input('Введите имя владельца:')
    while True:
        print(show_shelves())
        shelf_number = input('{} {}'.format(
            'На какую полку поместить документ',
            '(as - добавить новую полку):'))
        if shelf_number == 'as':
            shelf_number = add_shelf(once=True)
        elif shelf_number in directories.keys():
            add_prompt = input('{} {} {}'.format(
                'Зарегистрировать документ {}, {}, {}'.format(
                document_id,
                document_type,
                document_owner),
                'и поместить его на полку {}'.format(shelf_number),
                '(Enter - ДА, любой другой символ - НЕТ):'))
            if add_prompt == '':
                pass
            else:
                return True
        else:
            print('Нет такой полки.')
            continue
        documents.append(dict([
                    ('type', document_type), 
                    ('number', document_id), 
                    ('name', document_owner)]))
        directories[shelf_number].append(document_id)
        show_list()
        break
    return True

def delete_document_from_shelf(document_id):
    for shelf, documents in directories.items():
        for document in documents:
            if document_id in document:
                documents.remove(document)
                return True

def delete_document_from_documents(document_id):
    for document in documents:
        if document_id in document['number']:
            documents.remove(document)

def delete_document():
    while True:
        document_id = input('Введите номер документа (q - для выхода):')
        if document_id == 'q':
            return True
        found_documents = show_list(document_id)
        if len(found_documents) == 1:
            delete_prompt = input('{} {}'.format(
                'Удалить документ {} ?'.format(found_documents[0]), 
                '(Enter - ДА, любой другой символ - НЕТ)'))
            if delete_prompt == '':
                delete_document_from_shelf(document_id)
                delete_document_from_documents(document_id)
                print('Документ удален.')
                return True
        else:
            print('По запросу найдено документов: {},'.
                format(len(found_documents)), 
                'уточните запрос...')
    
def move_document():
    while True:
        document_id = input('Введите номер документа (q - для выхода):')
        if document_id == 'q':
            return True
        found_documents = show_list(document_id)
        if len(found_documents) == 1:
            while True:
                print(show_shelves())
                shelf_number = input('{} {}'.format(
                    'На какую полку переместить документ {} ?'.
                        format(found_documents[0]),
                    '(as - добавить новую полку):'))
                if shelf_number == 'as':
                    shelf_number = add_shelf(once=True)
                elif shelf_number in directories.keys():
                    if found_documents[0] in directories[shelf_number]:
                        print('Документ уже нахожится на {} полке'.
                            format(shelf_number))
                        continue
                    else:
                        move_prompt = input('{} {} {}'.format(
                            'Переместить документ {}'.format(found_documents[0]),
                            'на полку {} ?'.format(shelf_number),
                            '(Enter - ДА, любой другой символ - НЕТ):'))
                        if move_prompt == '':
                            delete_document_from_shelf(document_id)
                            directories[shelf_number].append(found_documents[0])
                            print('Документ перемещен.')
                            return True
                else:
                    print('Нет такой полки.')
                    continue
        else:
            print('По запросу найдено документов: {},'.
                format(len(found_documents)), 
                'уточните запрос...')


def show_shelves():
    return 'Есть полки с номерами: {}'.format(', '.join(directories.keys()))
    
def add_shelf(once=False):
    while True:
        print(show_shelves())
        shelf_number = input('Введите номер новой полки (q - для выхода):')
        if shelf_number == 'q':
            return True
        try:
            if str(int(shelf_number)) in directories.keys():
                print('Полка с таким номером уже есть!')
            else:
                directories[shelf_number] = list()
                if once:
                    return shelf_number
        except:
            print('Введите целое число!')
    return True

choices = {
    'q': exit,
    'h': show_commands,
    'p': show_people,
    'l': show_list,
    's': show_shelf,
    'a': add_document,
    'd': delete_document,
    'm': move_document,
    'as': add_shelf
}

while True:
    user_choice = input('{} {}'.format(
        'Введите команду', 
        '(например, q - для выхода или h - для справки):'))
    try:
        if not choices[user_choice]():
            break
    except:
        pass
        
        
        