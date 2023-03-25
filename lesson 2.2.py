import random
class Student():
    def __init__(self, name,):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 100
        self.alive = True


    def is_alive(self):
        if self.progress <= -0.5:
            print('Cast out')
            self.alive = False
        if self.money <= 0:
            print('No Money')
            self.alive = False
        if self.gladness <= 0:
            print('depression. You need go to the computer club')
            self.alive = False
        if self.progress > 5:
            print('You win')
            self.alive = False

    def end_of_day(self):
        print(f'Gladness = {self.gladness}')
        print(f'Progress = {round(self.progress, 2)}')
        print(f'money = {self.money}')

    def live(self,day):
        day = f'Day #{day} of {self.name} life!'
        print(f'{day:=^50}')

        self.end_of_day()
        self.is_alive()
        self.zalet()

    def zalet(self):
        for i in range (1, 2,):
            if self.progress <0.5:
                self.to_study()
            if self.money < 90:
                self.to_study()
            if self.gladness < 30:
                self.to_chill()
    def to_study(self):
        print('Time to study')
        self.progress += 0.12
        self.gladness -= 3
        self.money += 100
    def to_sleap(self):
        print('Time to sleep')
        self.gladness += 3
    def to_chill(self):
        print('Time to chill')
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 50


egor = Student(name='Egor')

for day in range(365):
    if egor.alive:
        egor.live(day)
    else:
        print('The end!')
        break






