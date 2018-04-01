import chardet

def get_words_from_file(filename) -> list:
    words_list = []
    with open(filename) as text_file:
        for line in text_file:
            # words_list.append(line)
            chardet.detect(line)
    return words_list


print(get_words_from_file("newsafr.txt"))
