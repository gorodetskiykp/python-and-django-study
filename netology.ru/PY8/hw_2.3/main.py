import json

files = [
    {'file_name': 'newsafr.json', 'code_page': 'utf-8'},
    {'file_name': 'newscy.json', 'code_page': 'koi8_r'},
    {'file_name': 'newsfr.json', 'code_page': 'cyrillic'},
    {'file_name': 'newsit.json', 'code_page': 'cp1251'},
]

if __name__ == '__main__':

    for news_block in files:
        with open( news_block['file_name'], 'r',
                   encoding=news_block['code_page'] ) as file:
            news = json.loads(file.read())

        words = {}
        for item in news['rss']['channel']['items']:
            for word in item['description'].split():
                if len(word) > 6:
                    word = word.lower()
                    if word in words:
                        words[word] += 1
                    else:
                        words.setdefault(word, 1)

        words_sorted_keys = sorted(words, key=words.get, reverse=True)
        print('\n{:-^30}'.format(news_block['file_name']))
        for number, word in enumerate(words_sorted_keys[:10]):
            print('{:>2}. {}'.format(number+1, word))