import subprocess
import os

def get_files_list(source_directory):
    # Получает директорию (относительный путь)
    # Возвращает список файлов директории
    return [image for image in os.listdir('Source') if '.jpg' in image.lower()]

def resizer(source_dir, result_dir):
    # Получает имена директорий исходников и результатов
    # Производит преобразование файлов
    if result_dir not in os.listdir():
        os.mkdir(result_dir)    
    for image in get_files_list(source_dir):
        source_image = os.path.join(source_dir, image)
        result_image = os.path.join(result_dir, image)
        subprocess.Popen(['convert', source_image, '-resize', '200', result_image])   

if __name__ == "__main__":
    source_dir = 'Source'
    result_dir = 'Result'
    resizer(source_dir, result_dir)
