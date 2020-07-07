"""
Вам дана строка и два маркера (начальный и конечный). Вам необходимо найти текст, заключенный между двумя этими маркерами. Но есть несколько важных условий.
Это упрощенная версия миссии Between Markers.
Начальный и конечный маркеры всегда разные.
Начальный и конечный маркеры всегда размером в один символ.
Начальный и конечный маркеры всегда есть в строке и идут один за другим.
Input: Три аргумента. Все строки. Второй и третий аргументы это начальный и конечный маркеры.
Output: Строка.
Пример:
    between_markers('What is >apple<', '>', '<') == 'apple'
Как это используется: Может использоваться для парсинга небольшой верстки.
Предусловия: Не может быть более одного маркера одного типа.
"""


def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    return text[text.index(begin)+1:text.index(end)]
    # return text[text.find(begin)+1:text.find(end)]


# def between_markers(text: str, begin: str, end: str) -> str:
#     for i in range(len(text)):
#         if text[i] == begin:
#             start = i + 1
#         elif text[i] == end:
#             stop = i 
#         else:
#             continue
#     return text[start:stop]


# import re
# def between_markers(text: str, begin: str, end: str) -> str:
#     return re.search(rf"\{begin}(.*?)\{end}", text).group(1)


# def between_markers(text: str, begin: str, end: str) -> str:
#     return (text.split(begin))[1].split(end)[0]


# between_markers = lambda text, begin, end: text.split(begin)[1].split(end)[0]


# between_markers = lambda x,y,z : __import__('re').search(f'(?<=[{y}]).*(?=[{z}])', x).group(0)


# between_markers = lambda t, b, e, f=lambda x,y: x.find(y): t[f(t,b)+1:f(t,e)]


# def between_markers(text: str, begin: str, end: str) -> str:
#     left, middle, right = text.partition(begin)
#     left, middle, right = right.partition(end)
#     return left


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"