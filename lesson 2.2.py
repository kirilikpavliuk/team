import random


class Student:
    def __init__(self, name,):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def is_alive(self):
        if self.progress <= -0.5:
            print('Cast out')
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
    def live(self,day):
        day = f'Day #{day} of {self.name} life!'
        print(f'{day:=^50}')
        cube = random.randint(1, 3)
        if cube == 1:
            self.to_study()
        elif cube == 2:
            self.to_chill()
        else:
            self.to_sleep()
        self.end_of_day()
        self.is_alive()
    def to_study(self):
        print('Time to study')
        self.progress += 0.12
        self.gladness -= 3
    def to_sleap(self):
        print('Time to sleep')
        self.gladness += 3
    def to_chill(self):
        print('Time to chill')
        self.gladness += 5
        self.progress -= 0.1


egor = Student('Egor')

for day in range(365):
    if egor.alive:
        egor.live(day)
    else:
        print('The end!')
        break







