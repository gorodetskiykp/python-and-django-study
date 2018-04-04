import os, subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))    


def get_images(source_path):
    images_path = os.path.join(BASE_DIR, source_path)
    for image_file in os.listdir(images_path):
        yield os.path.join(images_path, image_file)


def resize_image(image_file, result_dir):
    if result_dir not in os.listdir(BASE_DIR):
        os.mkdir(os.path.join(BASE_DIR, result_dir))
    result_file = os.path.join(BASE_DIR, result_dir, os.path.split(image_file)[-1])
    subprocess.Popen(['convert', image_file, '-resize', '200', result_file])
    return result_file


def main():
    source_dir_name = 'Source'
    result_dir_name = 'Result'
    for image_file in get_images(source_dir_name):
        resize_image(image_file, result_dir_name)


if __name__ == "__main__":
    main()
