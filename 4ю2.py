
class Class1:
    var = 20

    def __init__(self):
        self.var
class Class2(Class1):
    def __init__(self):
        print(self.var)
        super().__init__()
        print(self.var)
        print(super().var)
