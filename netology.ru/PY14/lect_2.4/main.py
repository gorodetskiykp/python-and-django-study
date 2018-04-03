import os
import chardet


def get_user_search_string():
    search_string = input("Введите строку для поиска: ")
    return search_string.strip()


def get_files(path):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    files_path = os.path.join(BASE_DIR, path)
    files_list = []
    for file_name in os.listdir(files_path):
        if '.sql' in file_name:
            files_list.append(os.path.join(files_path, file_name))
    return files_list


def search_in_file(file_name, searched_text):
    with open(file_name) as searched_file:
        if searched_text in searched_file.read():
            return True
    return False


def main():
    files_list = get_files('2.3-paths/Migrations')
    while True:
        local_files_list = files_list[:]
        files_list = []
        search_string = get_user_search_string()
        for file_name in local_files_list:
            if search_in_file(file_name, search_string):
                files_list.append(file_name)
                print(os.path.split(file_name)[-1])
        print("Всего: {}".format(len(files_list)))


if __name__ == "__main__":
    main()
