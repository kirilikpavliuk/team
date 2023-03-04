class Student:
    def sayHi(self):
        print(f'Hi! I`m {self.name}')
    def __init__(self, name, height):
        self.name = name
        self.height = height
    def __str__(self):
        return self.name
sergui = Student('Sergui', 180)
anton = Student('Anton', 160)

sergui.sayHi()
anton.sayHi()

print(sergui.height)
print(anton.height)
