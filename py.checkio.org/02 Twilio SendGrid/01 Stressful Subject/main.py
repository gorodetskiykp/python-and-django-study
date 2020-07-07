"""
У Софии был очень напряженный месяц и она решила взять отпуск на неделю. 
Чтобы избежать стресса во время отпуска, она хочет перенаправлять Стивену электронные письма со стрессовыми темами.
Функция должна распознавать является ли тема письма стрессовой. 
Стрессовая тема определяется тем, что все буквы в верхнем регистре, 
и / или заканчиваются как минимум тремя восклицательными знаками, 
и / или содержат по крайней мере одно из следующих слов-маркеров: "help", "asap", "urgent". 
Любое из этих слов-маркеров может быть написано по-разному: «HELP», «help», «HeLp», «H! E! L! P!», «H-E-L-P», и даже очень непринужденно «HHHEEEEEEEEELLP».
Входные данные: Тема письма в виде строки.
Выходные данные: Boolean.
Пример:
    is_stressful("Hi") == False
    is_stressful("I neeed HELP") == True
Предварительное условие: Тема может содержать до 100 букв.
"""

import re

def is_stressful(subj: str) -> bool: 
    if subj.isupper() or subj.endswith("!!!"):
        return True
    markers = ("help", "asap", "urgent")
    subj = re.sub(r'[\s+\W]', '', subj).lower()
    subj_letters = []
    prev_letter = ""
    for letter in subj:
        if letter != prev_letter:
            subj_letters.append(letter)
        prev_letter = letter
    subj = ''.join(subj_letters)
    return any([marker in subj for marker in markers])

if __name__ == '__main__':
    print(is_stressful("Hi"))
    print(is_stressful("I need help"))

    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"