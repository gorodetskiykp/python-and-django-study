class Alive:

    color = 'Серый'
    paws = 4
    sound_like = 'Pshsh..'
    weight = 0
    name = 'it'
    kind = 'Живое'

    def sound(self):
        print('{} сказал: "{}"'.format(self.name, self.sound_like))

    def __str__(self):
        return 'Вид: {}\nИмя: {}\nВес: {}\nЦвет: {}\nКоличество лап: {}'.\
            format(self.kind, self.name, self.weight, self.color, self.paws)


class Animal(Alive):

    def __init__(self, kind='Животное', name='Дружок'):
        self.kind = kind
        self.name = name

    gives_milk = False


class Bird(Alive):

    def __init__(self, kind='Птица', name='Чижик'):
        self.kind = kind
        self.name = name

    paws = 2
    can_fly = True


if __name__ == '__main__':

    cow = Animal('Корова', 'Зойка')
    cow.weight = 120
    cow.sound_like = 'Муууу..'
    cow.gives_milk = True
    print(cow)
    cow.sound()
    print()
    goat = Animal('Коза', 'Зинка')
    goat.weight = 45
    goat.sound_like = 'Бее..'
    goat.gives_milk = True
    print(goat)
    goat.sound()
    print()
    sheep = Animal('Овца', 'Минька')
    sheep.weight = 60
    sheep.sound_like = 'Мее..'
    sheep.gives_milk = False
    sheep.color = 'Белый'
    print(sheep)
    sheep.sound()
    print()
    duck = Bird('Утка', 'Утка')
    duck.weight = 12
    duck.sound_like = 'Крак-крак..'
    duck.color = 'Черный'
    print(duck)
    duck.sound()