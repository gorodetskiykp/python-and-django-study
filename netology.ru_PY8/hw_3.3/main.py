import os
from practice import translate_it

if __name__ == '__main__':
    lang_to = 'ru'
    if 'results' not in os.listdir():
        os.mkdir('results')
    for fl_file in os.listdir('sources'):
        source_file = os.path.join('sources', fl_file)
        with open(source_file, 'r', encoding='utf8') as f_read:
            lang_from = fl_file[:-4].lower()
            translated = translate_it(f_read.read(), '{}-{}'.format(lang_from, lang_to))
            result_file = os.path.join('results', fl_file)
            with open(result_file, 'w', encoding='utf8') as f_write:
                f_write.write(translated)
