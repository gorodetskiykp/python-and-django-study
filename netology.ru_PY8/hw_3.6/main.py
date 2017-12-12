class Alive:

    color = 'Серый'
    paws = 4
    sound_like = 'Pshsh..'
    weight = 0
    name = 'it'

    def sound(self):
        print('{} сказал: "{}"'.format(self.name, self.sound_like))

    def __str__(self):
        return 'Имя: {}\nВес: {}\nЦвет: {}\nКоличество лап: {}'.\
            format(self.name, self.weight, self.color, self.paws)


class Animal(Alive):

    def __init__(self, name='Животное'):
        self.name = name

    gives_milk = False


class Bird(Alive):

    def __init__(self, name='Чижик'):
        self.name = name

    paws = 2
    can_fly = True


class Cow(Animal):
    sound_like = 'Мууу...'
    weight = 120
    gives_milk = True


class Goat(Animal):
    sound_like = 'Беее...'
    weight = 40
    gives_milk = True


class Sheep(Animal):
    
    def __init__(self):
        self.name = 'Долли 4'

    sound_like = 'Меее...'
    weight = 45
    gives_milk = True


if __name__ == '__main__':

    print()
    cow = Cow('Зойка')
    print(cow.__class__)
    print(cow)
    cow.sound()
    print()
    goat = Goat('Зинка')
    print(goat.__class__)
    goat.color = 'Белый'
    print(goat)
    goat.sound()
    print()
    sheep = Sheep()
    print(sheep.__class__)
    print(sheep)
    sheep.sound()
