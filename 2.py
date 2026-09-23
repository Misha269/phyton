import random


class Human:
    def __init__(self, name, car=None):
        self.name = name
        self.car = car
        self.house = House()
        self.money = 100
        self.alive = True

    def work(self):
        self.money += random.randint(8, 15)
        if self.car == None:
            print("Пішли працювати пішки")
        else:
            if self.car.drive(random.randint(7, 15)):
                print("Поїхали працювати на авто")
            else:
                print("Немає бензину, пішли пішки")

    def shopping(self):
        self.money -= random.randint(5, 10)
        if self.car == None:
            print("Пішли на шопінг пішки")
        else:
            if self.car.drive(random.randint(10, 20)):
                print("Поїхали на шопінг на авто")
            else:
                print("Немає бензину, пішли пішки")

    def eat(self):
        print("Я покушав")
        self.money -= random.randint(2, 4)
        self.house.food -= 3


    def info(self):
        print(f"сьогодні {self.name} мае")
        print(f"гроші: {self.money}")

    def is_alive(self):
        if self.money <= 0:
            print("я бомж")
            self.alive = False

    def live(self, day):
        print(f"День №{day} з життя {self.name}")
        print("-"*30)

        func = [self.shopping, self.eat, self.work]
        random.choice(func)()

        self.info()
        self.is_alive()
        print()


class Car:
    def __init__(self, model):
        self.model = model
        self.fuel = 60
        self.state = 100

    def drive(self, length):
        delta_fuel = length * 0.1
        if self.fuel - delta_fuel > 0:
            print(f"Ми проїхали {length} км, виратили {delta_fuel} л пального")
            self.fuel -= delta_fuel
            self.state -= length * 0.01
            return True
        else:
            print("Подорож неможлива, не вистачає пального")
            return False

    def add_fuel(self):
        if self.fuel <= 0:
            print("треба піти заправити машину")
            self.fuel += random.randint(5, 60)

    def info(self):
        print(f"пальне: {self.fuel}")
        print(f"стан машини: {self.state}")

    def __str__(self):
        return f"Авто: {self.model}, пальне: {self.fuel} л, стан {self.state} %"


class House:
    def __init__(self):
        self.food = 20
        self.pollution = 20

    def chill(self):
        print("треба отдіхнути")
        self.pollution -= random.randint(2, 5)

    def cleaning(self):
        print("Треба прибратись")
        self.pollution += 3

    def shopping(self):
        self.food += random.randint(1, 10)
        if self.car == None:
            print("Пішли на шопінг пішки")
        else:
            if self.car.drive(random.randint(10, 20)):
                print("Поїхали на шопінг на авто")
            else:
                print("Немає бензину, пішли пішки")

    def is_alive(self):
        if self.food <= 0:
            print("я голодний")
            self.alive = False

    def info(self):
        print(f"їжа: {self.food}")
        print(f"чистота: {self.pollution}")
    def __str__(self):
        return f"Дім: {self.food} їжі, чистота: {self.pollution}"

    def live(self, day):
        print(f"День №{day} з життя {self.name}")
        print("-"*30)

        func = [self.cleaning, self.shopping, self.chill,]
        random.choice(func)()

        self.info()
        self.is_alive()
        print()

human = Human("Mogg")
for day in range(365):
    if not human.alive:
        break
    human.live(day)