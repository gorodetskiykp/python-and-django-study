import chardet

#def get_news(file_name, file_code_page='utf8') -> str:
#    with open(file_name, encoding=file_code_page) as text_file:
#        return text_file.read()

def get_news(file_name) -> str:
    text_file = open(file_name, 'r')
    code_page = chardet.detect(text_file)['encoding']
    return text_file.encode(code_page)
        
        
def get_top_words(text, word_length=6, top_range=10):
    words = {}
    for word in text.split():
        if len(word) > word_length:
            word = word.lower()
            try:
                words[word] += 1
            except KeyError:
                words.setdefault(word, 1)
    common_words = sorted(words.items(), key=lambda value: value[1], reverse=True)[:top_range]
    return [word[0] for word in common_words]


def main():
    files = [
        #{'name': 'newsafr.txt', 'code_page': 'utf8'},
        #{'name': 'newscy.txt', 'code_page': 'koi8-r'},
        {'name': 'newsfr.txt', 'code_page': 'cp866'},
        #{'name': 'newsit.txt', 'code_page': 'cp1251'},
    ]
    
    for news_file in files:
        news_text = get_news(news_file['name'])
        print("{}: {}".format(news_file['name'], ', '.join(get_top_words(news_text))))


if __name__ == "__main__":
    main()
