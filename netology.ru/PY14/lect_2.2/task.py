import chardet


def get_news(file_name):
    with open(file_name, 'rb') as text_file:
        raw_text = text_file.read()
        code_page = chardet.detect(raw_text)['encoding']
    return raw_text.decode(code_page)

        
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
    files = ['newsafr.txt', 'newscy.txt', 'newsfr.txt', 'newsit.txt']
    
    for news_file in files:
        news_text = get_news(news_file)
        print("{}: {}".format(news_file, ', '.join(get_top_words(news_text))))


if __name__ == "__main__":
    main()
