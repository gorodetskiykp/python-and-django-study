import os
import re

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))
abs_path = os.path.join(current_dir, migrations)

def files_reader():
    """Возвращает список sql-файлов в директории."""
    all_files = os.listdir(abs_path)
    return [file_name for file_name in all_files if file_name.endswith('.sql')]

def find_word(file_name, word, case_insensitive=True):
    """Ищет слово в файле.
    Возвращает True, если слово найдено.
    Аргументы:
    file_name - файл, в котором нужно искать
    word - слово, которое нужно искать
    case_insensitive - регистронезависимый поиск (по умолчанию True)
    """
    with open(os.path.join(abs_path, file_name), 'r', encoding='cyrillic') as parsed_file:
        text = parsed_file.read()
        text = re.sub(r'\W', '', text)
        if case_insensitive:
            return word.lower() in text.lower()
        else:
            return word in text

def find_files_in_list(files_list, word):
    """Фильтрует список файлов по искомому слову.
    Возвращает отфильтрованный список файлов.
    Аргументы:
    file_list - список имен файлов
    word - слово, по которому идет фильтация списка
    """
    new_files_list = []
    for file_name in files_list:
        if find_word(file_name, word):
            new_files_list.append(file_name)
    return new_files_list

if __name__ == '__main__':
    files = files_reader()
    while True:
        word = input('Введите строку: ')
        files = find_files_in_list(files, word)
        print('\n'.join(files))
        result_len = len(files)
        print('Всего: {}'.format(result_len))
        if result_len == 0:
            break
