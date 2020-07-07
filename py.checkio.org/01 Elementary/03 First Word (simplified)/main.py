"""
Дана строка и нужно найти ее первое слово.
Строка состоит только из английских символов и пробелов.
В начале и в конце строки пробелов нет.
Входные параметры: Строка.
Выходные параметры: Строка.
Пример:
first_word("Hello world") == "Hello"
Условие: Текст может содержать строчные, прописные буквы и пробелы.
"""

def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    return text.split()[0]


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))
    
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"