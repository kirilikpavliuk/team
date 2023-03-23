class Grandparent:
    height = 150
    age = 60
    eyes_color = 'Blue'

    def print_values(self):
        print(f'{self} Atributes:')
        print(self.height)
        print(self.eyes_color)
        print(self.age)


class Parent(Grandparent):
    height = 170
    eyes_color = 'Green'


class Hello_World:
    hello = 'Hello'
    _hello = '_Hello'
    __hello = '__Hello'

    def __init__(self):
        self.world = 'World'
        self._world = '_World'
        self.__world = '__World'

    def printer(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.world)
        print(self._world)
        print(self.__world)

class Hello_World2(Hello_World):
    pass

class Child(Parent):
    age = 15


bob = Parent()
anton = Child()
mark = Grandparent()
mark.print_values()
bob.print_values()
anton.print_values()

hw = Hello_World
hw2  = Hello_World2
hw.printer()