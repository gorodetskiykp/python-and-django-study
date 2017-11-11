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
    kind = 'Животное'

    def __init__(self, name='Дружок'):
        self.name = name

    gives_milk = False


class Bird(Alive):
    kind = 'Птица'

    def __init__(self, name='Чижик'):
        self.name = name

    paws = 2
    can_fly = True


class Cow(Animal):
    kind = 'Корова'
    sound_like = 'Мууу...'
    weight = 120
    gives_milk = True

if __name__ == '__main__':

    cow = Cow('Зойка')
    print(cow)
    cow.sound()
    print()
    goat = Animal('Зинка')
    goat.kind = 'Коза'
    goat.weight = 45
    goat.sound_like = 'Бее..'
    goat.gives_milk = True
    print(goat)
    goat.sound()
    print()
    sheep = Animal('Минька')
    sheep.kind = 'Овца'
    sheep.weight = 60
    sheep.sound_like = 'Мее..'
    sheep.gives_milk = False
    sheep.color = 'Белый'
    print(sheep)
    sheep.sound()
    print()
    duck = Bird('Утка')
    duck.weight = 12
    duck.sound_like = 'Крак-крак..'
    duck.color = 'Черный'
    print(duck)
    duck.sound()
