import requests
import os
import re

def translate_it(text, lang_params):
    """
    YANDEX translation plugin

    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/

    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'

    params = {
        'key': key,
        'lang': lang_params,
        'text': text,
    }
    response = requests.get(url, params=params).json()
    return ' '.join(response.get('text', []))


def translate_file(input_file_name, output_file_name, input_language, output_language='ru'):
    with open(input_file_name) as input_file:
        input_file_text = input_file.read()
    lang_params = '{}-{}'.format(input_language, output_language)
    print(lang_params)
    translated_text = translate_it(input_file_text, lang_params) 
    with open(output_file_name, 'w') as output_file:
        output_file.write(translated_text)


def main():
    #a = translate_it('Привет')
    #print(a)
    output_language = 'ru'
    for file_name in os.listdir():
        if re.match(r'^[A-Z]{2}.txt$', file_name): 
            input_language = file_name.split('.')[0].lower()
            translate_file(file_name, '{}-{}.txt'.format(input_language.upper(), output_language.upper()), input_language, output_language)


if __name__ == "__main__":
    main()
