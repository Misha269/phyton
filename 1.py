import random

class Student:
    def __init__(self, name):
        self.name = name
        self.progress = 10
        self.gladness = 30
        self.energy = 50
        self.alive = True
        self.money = 100

    def study(self):
        print("Я пішов до академії IT STEP")
        self.progress += 3
        self.energy -= 1
        self.gladness -= 3
        self.money -= 2

    def chill(self):
        print("Я пішов з друзяками гулять")
        self.gladness += 2
        self.energy -= 2
        self.progress -= 3
        self.money -= 3

    def sleep(self):
        print("Я пішов спати")
        self.energy += 3
        self.gladness += 2

    def eat(self):
        print("Чіпси та кола - наші найкращі друзі :)")
        self.energy += 3
        self.gladness += 2
        self.money -= 3

    def work(self):
        print("Я пішов працювати")
        self.energy -= 2
        self.gladness -= 1
        self.progress += 2
        self.money += 7


    def is_alive(self):
        if self.gladness <= 0:
            print("В мене дипресія :(")
            self.alive = False
        if self.energy <= 0:
            print("Я зовсім знесилений :(")
            self.alive = False
        if self.progress <= 0:
            print("В мене в голові суцільне сміття :(")
            self.alive = False
        if self.progress > 100:
            print("Я геній. Достроково закінчив академію IT STEP :)")
            self.alive = False
        if self.money <= 0:
            print("Я бомж")
            self.alive = False



    def live(self, day):
        print(f"День №{day} з життя {self.name}")
        print("-"*30)

        func = [self.study, self.sleep, self.eat, self.chill, self.work]
        random.choice(func)()

        self.info()
        self.is_alive()
        print()

    def info(self):
        print(f"На сьогодні {self.name} має:")
        print(f"Задоволення : {self.gladness}")
        print(f"Знання      : {self.progress}")
        print(f"Енергія     : {self.energy}")
        print(f"Гроші       : {self.money}")


student = Student("Mogg")
for day in range(366):
    if not student.alive:
        break
    student.live(day)