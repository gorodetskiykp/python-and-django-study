""""
1. Что такое Zen of Python?
>> Свод настоятельных рекомендаций по стилю программирования для python-разработчиков.
Философия программирования на Python.
Документация стандартных библиотек Python.
"""

"""
2. Каким количеством отступов (пробелов) разделяют блоки кода?
1
2
3
>> 4
5
6
"""

"""
3. Рекомендованная максимальная длина строки кода?
50 или 100 символов
30 или 80 символов
>> 80 или 120 символов
100 или 160 символов
"""

"""
4. Выберите варианты БЕЗ ошибок в имени(-ах) объектов:
def GreatOne:           - Invalid function name "GreatOne" (invalid-name)
class My_super_class:   - Invalid class name "My_super_class" (invalid-name)
>> NAME = 'Robin'
>> def great_one:
>> class MySuperClass:
class mySuperClass:     - Invalid class name "mySuperClass" (invalid-name)
>> x = y + z
def GREAT_ONE:          - Invalid function name "GREAT_ONE" (invalid-name)
"""

"""
5. Вам представлены куски кода, выберите варианты БЕЗ стилистических ошибок:
a = (1,2,3,4,5)                             - Exactly one space required after comma
if 123==45 or 'ben' in kings:               - Exactly one space required around comparison
>> x, y = (25, 45)
foo = {'A':56, 'B':77}                      - E231 missing whitespace after ':'
>> def goo(param, x=0):
my_dict = {'Great' :'Ben', 'Small :'None'}  - E203 whitespace before ':'
>> hello = [34, 55, 67]
"""

"""
6. Вам представлены куски кода, выберите варианты БЕЗ стилистических ошибок:

ALL = (                     <<
  'Boris', 'Anna',
  'Lena', 'Ron',
)

a = (1, 2, 3, 4, 5,         - E128 continuation line under-indented for visual indent
6, 7, 8, 9, 10)

a = (1 + 2 + 3 + 4 + 5      - W503 line break before binary operator
    + 6 + 7 + 8 + 9 + 10)

def foo(param1, param2,     - E128 continuation line under-indented for visual indent
    name, text):

b = [5, 4, 3,               - E128 continuation line under-indented for visual indent
    2, 1, 0]

class A:                    <<
    def _example1(self):
        pass

    def __example2(self):
        pass

def boo(high,               - E128 continuation line under-indented for visual indent
low, mid):

""One, Two, Three,          <<
Four, Five, Six
""
"""

"""
7. Выберите варианты, где print(foo) вернет True (где foo == True):

a = 1,                      
foo = isinstance(a, int)
print(foo)                  - False

a = 3,
foo = isinstance(a, tuple)
print(foo)                  - True

a = ""
foo = bool(a)
print(foo)                  - False

a = 0.0
foo = bool(a)
print(foo)                  - False

a = [""]
foo = bool(a)
print(foo)                  - True

a = " "
foo = bool(a)
print(foo)                  - True

a = None
foo = bool(a)
print(foo)                  - False

a = (None,)
foo = bool(a)
print(foo)                  - True

a = dict()
foo = bool(a)
print(foo)                  - False
"""

"""
8. Вам представлены куски кода, выберите варианты БЕЗ стилистических ошибок:

def foo(x, y):                                          <<
    pass                                                <<
                                                        <<
                                                        <<
my_function()                                           <<
text = foo(x, y)                                        <<

def foo(x, y):
    pass
my_function()
text = foo(x, y); name = foo(t, r); label = foo(d, c)   - E702 multiple statements on one line (semicolon)

if True: continue                                       <<
my_function()                                           <<

if True: name = 'Jack'; my_function(); c = 1 + 4        - E701 multiple statements on one line (colon)

if number != 22:                                        <<
    break                                               <<
my_function()                                           <<
"""

"""
9. Какие задачи решают docstrings?
>> Как использовать данный кусок кода; описание параметров (для функции); возвращаемые значения (для функции); возвращаемые исключения (функции). Пишется для пользователя.
Хранит информацию о разработчике и ссылка на его фотографию.
Рациональное объяснение данного куска кода; как работает эта часть кода; что еще стоит дописать или улучшить на этом участке кода. Пишутся для разработчиков.
Хранит ссылку на репозиторий в github.

10. Используя List Comprehensions, получить list из кубов всех чисел, делящихся и на 3, и на 4 без остатка, взятых из массива чисел mass.

Пример ответа:
[x for x in mass]
"""

mass = range(100)
print([x for x in mass if x % 3 == 0 and x % 4 == 0])