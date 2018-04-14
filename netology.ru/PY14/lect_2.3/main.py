import json
import chardet
import xml.etree.ElementTree as ET

def open_file(file_name):
    """
    читает файл
    принимает имя файла и кодировку
    возвращает текст файла
    """
    with open(file_name, 'rb') as parsing_file:
        code_page = chardet.detect(parsing_file.read())['encoding']
    with open(file_name, encoding=code_page) as parsing_file:
        return parsing_file.read()


def get_news(text, text_struct):
    """
    извлекает текст новости
    принимает текст и структуру (json, xml)
    возвращает список новостей (только тексты)
    """
    news_list = []
    if text_struct == 'json':
        file_text = json.loads(text)
        for item in file_text['rss']['channel']['items']:
            news_list.append(item['description'])
    elif text_struct == 'xml':
        root = ET.fromstring(text)
        items = root.find('channel').findall('item')
        for item in items:
            news_list.append(item[2].text)
    return news_list


def get_long_words(words_list, word_length=6):
    """
    извлекает длинные слова
    принимает список предложений и длину слова
    возвращает список слов больше заданной длины
    """
    long_words_list = []
    for text in words_list:
        for word in text.split():
            if len(word) > word_length:
                long_words_list.append(word.lower())
    return long_words_list


def get_words_frequecny(words_list):
    """
    считает частоту употребления слов
    принимает список слов
    возвращает словарь "слово": количество
    """
    words_frequecny_dict = {}
    for word in words_list:
        try:
            words_frequecny_dict[word] += 1
        except KeyError:
            words_frequecny_dict.setdefault(word, 1)
    return words_frequecny_dict


def get_common_words(frequencies_dict, top_range=10):
    """
    ищет наиболее употребимые слова
    принимает словарь частот и ограничение на вывод самых употребимых слов
    возвращает список наиболее употребимых слов
    """
    top_common_words = sorted(frequencies_dict.items(), key=lambda value: value[1], reverse=True)[:top_range]
    return [word[0] for word in top_common_words]


def main():
    files = [
        "newsafr.json",
        "newsafr.xml",
        "newscy.json",
        "newscy.xml",
        "newsfr.json",
        "newsfr.xml",
        "newsit.json",
        "newsit.xml",
    ]

    for news_file in files:
        file_text = open_file(news_file)
        news_list = get_news(file_text, news_file.split('.')[1])
        words = get_long_words(news_list)
        words_frequecny = get_words_frequecny(words)
        top_frequecny_words = get_common_words(words_frequecny)
        print("{}: {}".format(news_file, ', '.join(top_frequecny_words)))


if __name__ == "__main__":
    main()
