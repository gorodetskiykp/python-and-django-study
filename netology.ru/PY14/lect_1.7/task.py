class Alive:
    
    def __init__(self):
        self.sound = "Aaarghh"
        self.paws = 4
        self.fly = False
        self.speed = 10
        self.name = "It"
        self.weight = 100
        self.jump = True
        
    
    def scream(self, sound=''):
        sound = sound if sound else self.sound
        print(sound)
        
    
    def run(self, speed=10):
        print("run")
        return speed
        
    
    def stop(self):
        print("stop")
        self.speed = 0
        return self.speed
        

class Animal(Alive):
    
    def __init__(self):
        super().__init__()
        self.sound = "Raaaaagh"
        self.speed = 20
        self.get_milk = True
        self.name = "Animal"
        self.weight = 150

    
class Bird(Alive):
    
    def __init__(self):
        super().__init__()
        self.sound = "Kraaaghh"
        self.paws = 2
        self.fly = True
        self.speed = 4
        self.fly_speed = 30 if self.fly else 0
        self.get_eggs = True
        self.name = "Bird"
        self.weight = 20
        

    def go_fly(self, fly_speed=30):
        if self.fly:
            print("I can fly!!")
            self.speed = self.fly_speed = fly_speed
        else:
            print("Sorry, I can't fly:(")
            self.fly_speed = fly_speed = 0
        return fly_speed
        
    
    def stop(self):
        print("stop")
        self.speed = 0
        self.fly_speed = 0
        return self.speed, self.fly_speed


class Cow(Animal):
    
    def __init__(self, name=''):
        super().__init__()
        self.sound = "Muuaghh"
        self.name = name if name else "Cow"
        self.jump = False
            

class Goat(Animal):
    
    def __init__(self, name=''):
        super().__init__()
        self.sound = "Beeeeakhh"
        self.name = name if name else "Goat"
        self.weight = 70


class Sheep(Animal):
    
    def __init__(self, name=''):
        super().__init__()
        self.sound = "Mmeeeeaa"
        self.name = name if name else "Dolli"
        self.weight = 80


class Pig(Animal):
    
    def __init__(self, name=''):
        super().__init__()
        self.sound = "Wuuuiiieaa"
        self.name = name if name else "Prapor"
        self.weight = 100
        self.jump = False
        self.speed = 10


class Duck(Bird):
    
    def __init__(self, name=''):
        super().__init__()
        self.sound = "Crackx"
        self.name = name if name else "Duffy"
        self.weight = 20
        self.jump = False


class Chicken(Bird):
    
    def __init__(self, name=''):
        super().__init__()
        self.sound = "Koookk"
        self.name = name if name else "Mippi"
        self.weight = 15
        self.jump = False
        self.fly = False
        

class Goose(Bird):
    
    def __init__(self, name=''):
        super().__init__()
        self.sound = "Ghaaah"
        self.name = name if name else "Mr. Goose"
        self.weight = 40
        self.jump = False
        self.fly = False
        

cow = Cow("Burjonka")
cow.scream()
print(cow.run())
print(cow.stop())
print(cow.name)
print(cow.run(5))
print(cow.get_milk)
print(cow.weight)
print(cow.jump)

print("-"*100)

goat = Goat()
goat.scream()
print(goat.name)
print(goat.weight)
print(goat.jump)

print("-"*100)

sheep = Sheep()
sheep.scream()
print(sheep.name)
print(sheep.weight)
print(sheep.jump)

print("-"*100)

pig = Pig()
pig.scream()
print(pig.name)
print(pig.weight)
print(pig.jump)

print("-"*100)

duck = Duck()
duck.scream()
print(duck.name)
print(duck.weight)
print(duck.jump)
print(duck.run())
print(duck.stop())
print(duck.go_fly(15))

print("-"*100)

chick = Chicken()
chick.scream()
print(chick.name)
print(chick.weight)
print(chick.jump)
print(chick.run())
print(chick.stop())
print(chick.go_fly(15))

print("-"*100)

goose = Goose()
goose.scream()
print(goose.name)
print(goose.weight)
print(goose.jump)
print(goose.run(15))
print(goose.stop())
print(goose.go_fly(15))
