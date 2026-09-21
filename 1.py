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
        self.progress += 1
        self.energy -= 1
        self.gladness -= 3

    def chill(self):
        print("Я пішов з друзяками гулять")
        self.gladness += 2
        self.energy -= 3
        self.progress -= 1

    def sleep(self):
        print("Я пішов спати")
        self.energy += 3
        self.gladness += 1

    def eat(self):
        print("Чіпси та кола - наші найкращі друзі :)")
        self.energy += 1
        self.gladness += 1

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


    def live(self, day):
        print(f"День №{day} з життя {self.name}")
        print("-"*30)

        func = [self.study, self.sleep, self.eat, self.chill]
        random.choice(func)()

        self.info()
        self.is_alive()
        print()

    def info(self):
        print(f"На сьогодні {self.name} має:")
        print(f"Задоволення : {self.gladness}")
        print(f"Знання      : {self.progress}")
        print(f"Енергія     : {self.energy}")


student = Student("Vasya")
for day in range(365):
    if not student.alive:
        break
    student.live(day)