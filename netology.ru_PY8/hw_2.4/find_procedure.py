import os

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))

def files_reader(abs_path):
    # Принимает абсолютный путь до директории
    # Возвращает список файлов в директории
    all_files = os.listdir(abs_path)
    return [file_name for file_name in all_files if '.sql' in file_name]

def find_word(file_name, word, abs_path):
    # Принимает имя файла и искомое слово
    # Можно передать абсолютный путь до файла
    # По умолсанию ищет в текущей директории
    # Возвращает True, если слово найдено в файле
    with open(os.path.join(abs_path, file_name), 'r', encoding='cyrillic') as parsed_file:
        return word in parsed_file.read()

def find_files_in_list(files_list, word, abs_path=''):
    # Получает список файлов
    # Возвращает список файлов, в которых найдено слово
    new_files_list = []
    for file_name in files_list:
        if find_word(file_name, word, abs_path):
            new_files_list.append(file_name)
    return new_files_list

if __name__ == '__main__':
    abs_path = os.path.join(current_dir, migrations)
    files = files_reader(abs_path)
    while True:
        word = input('Введите строку: ')
        files = find_files_in_list(files, word, abs_path)
        print('\n'.join(files))
        result_len = len(files)
        print('Всего: {}'.format(result_len))
        if result_len == 0:
            break

