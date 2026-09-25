import random


class Animal:
    def __init__(self):
        self.animals = 2
        self.alive = True
        self.mammals_group = Mammals()
        self.fish_group = Fish()

    def is_alive(self):

        if self.mammals_group.mammals == 0:
            self.animals -= 1

        if self.fish_group.fish == 0:
            self.animals -= 1

        if self.animals == 0:
            self.alive = False

    def info(self):
        print(f"Всього груп тварин залишилось: {self.animals}")

    def live(self, day):
        print(f"День №{day} з життя тварин")
        print("-" * 30)

        self.mammals_group.live_day()
        self.fish_group.live_day()

        self.mammals_group.is_alive()
        self.fish_group.is_alive()
        self.is_alive()

        self.mammals_group.info()
        self.fish_group.info()
        self.info()
        print()


class Mammals(Animal):
    def __init__(self):
        self.mammals = 2
        self.alive = True
        self.cat = Cat()
        self.dog = Dog()

    def live_day(self):
        self.cat.eat()
        self.dog.eat()

    def is_alive(self):
        self.mammals = 2
        if self.cat.food <= 0:
            self.mammals -= 1
        if self.dog.food <= 0:
            self.mammals -= 1
        if self.mammals == 0:
            self.alive = False

    def info(self):
        self.cat.info()
        self.dog.info()
        print(f"На сьогодні живі {self.mammals} ссавці(в)")


class Cat(Mammals):
    def __init__(self):
        self.food = 10

    def eat(self):
        self.food -= random.randint(1, 7)
        self.food += random.randint(2, 6)

    def info(self):
        print(f"Сьогодні у кота {self.food} їжі")


class Dog(Mammals):
    def __init__(self):
        self.food = 10

    def eat(self):
        self.food -= random.randint(1, 7)
        self.food += random.randint(2, 6)

    def info(self):
        print(f"Сьогодні у собаки {self.food} їжі")


class Fish(Animal):
    def __init__(self):
        self.fish = 1
        self.alive = True
        self.goldfish = GoldFish()  # Создаем рыбку

    def live_day(self):
        self.goldfish.eat()

    def is_alive(self):
        self.fish = 1
        if self.goldfish.food <= 0:
            self.fish -= 1
        if self.fish == 0:
            self.alive = False

    def info(self):
        self.goldfish.info()
        print(f"На сьогодні живі {self.fish} риб(и)")


class GoldFish(Fish):
    def __init__(self):
        self.food = 10
        self.alive = True

    def eat(self):
        self.food -= random.randint(1, 7)
        self.food += random.randint(2, 6)

    def info(self):
        print(f"Сьогодні у золотої рибки {self.food} їжі")


animal = Animal()
for day in range(1, 365):
    if not animal.alive:
        print("Всі тварини загинули. Симуляція завершена.")
        break
    animal.live(day)