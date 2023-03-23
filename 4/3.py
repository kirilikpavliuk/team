class Monitor:
    def __init__(self):
        super().__init__()
        self.resolution = '4K'
    def display(self):
        print('4k')

class Processor:
    def __init__(self):
        super().__init__()
        self.cores = 8
    def calculate(self):
        print('8 cores')



class Computer(Monitor,Processor):
    def info(self):
        print(self.cores)
        print(self.resolution)

asus = Computer()
asus.info()