print("Hello", "World!")
print("Hard Times"[5])
print("giraffe"[0])
print(int("45"))
print(str(912))

x = "blue"
y = "green"
z = x
print(x, y, z)
z = y
print(x, y, z)
x = z
print(x, y, z)

route = 866
print(route, type(route))
route = "North"
print(route, type(route))

countries = "Denmark", "Norway", "Sweden"
numbers = "one",
print(countries)
print(numbers)

list_1 = [1, 4, 9, 16, 25, 36, 49]
list_2 = ['alpha', 'bravo', 'charlie', 'delta', 'echo']
list_3 = ['zebra', 49, -879, 'aardvark', 200]
list_4 = []

print(len(("one", )))
print(len([3, 5, 1, 2, "pause", 5]))
print(len("automatically"))

x = list_3
print(x)
x.append("more")
print(x)
list.append(x, "extra")
print(x)
print(x[0])
print(x[4])
x[1] = "forty nine"
print(x)

a = ["Retention", 3, None]
b = ["Retention", 3, None]
print(a is b)
b = a
print(a is b)

a = "Something"
b = None
print(a is not None, b is None)

a = 2
b = 6
print(a == b)
print(a < b)
print(a <= b, a != b, a >= b, a > b)

a = "many paths"
b = "many paths"
print(a is b)
print(a == b)

a = 9
print('0 <= a <= 10 : {}'.format(0 <= a <= 10))

# print("three" < 4)
print('int("3") < 4 : {}'.format(int("3") < 4))

p = (4, "frog", 9, -33, 9, 2)
print('2 in p : {}'.format(2 in p))
print('"dog" not in p : {}'.format("dog" not in p))

phrase = "Peace is no longer permitted during Winterval"
print('"v" in phrase : {}'.format("v" in phrase))
print('"ring" in phrase : {}'.format("ring" in phrase))

five = 5
two = 2
zero = 0
print('five and two : {}'.format(five and two))
print('two and five : {}'.format(two and five))
print('five and zero : {}'.format(five and zero))
print('zero and five : {}'.format(zero and five))
nought = 0
print('five or two : {}'.format(five or two))
print('two or five : {}'.format(two or five))
print('zero or five : {}'.format(zero or five))
print('zero or nought : {}'.format(zero or nought))

if x:
    print("x is nonzero")

lines = 1200
if lines < 1000:
    print("small")
elif lines < 10000:
    print("medium")
else:
    print("large")

# while True:
#     item = get_next_item()
#     if not item:
#         break
#     process_item(item)

for country in ["Denmark", "Norway", "Sweden"]:
    print('country - {}'.format(country))

for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    if letter in "AEIOU":
        print(letter, "is a vowel")
    else:
        print(letter, "is a consonant")

print('5 + 6 = {}'.format(5 + 6))
print('3 - 7 = {}'.format(3 - 7))
print('4 * 8 = {}'.format(4 * 8))
print('12 / 3 = {}'.format(12 / 3))
print('3 / 2 = {}'.format(3 / 2))

a = 5
print('a = {}'.format(a))
a += 8
print('a +=8 : {}'.format(a))

name = "John"
print('name + "Doe" : {}'.format(name + "Doe"))
name += " Doe"
print('name += " Doe" : {}'.format(name))

seeds = ["sesame", "sunflower"]
seeds += ["pumpkin"]
print('seeds : {}'.format(seeds))
# seeds += 5
seeds += [5]
print('seeds : {}'.format(seeds))
seeds += [9, 1, 5, "poppy"]
print('seeds : {}'.format(seeds))
seeds += "durian"
print('seeds : {}'.format(seeds))