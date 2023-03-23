import sys
import tkinter
import inspect
def first_func():
    pass

class First_class:
    def printer(self):
        pass
class Second_class (First_class):
    pass

tk = tkinter
first_f = first_func
first_c = First_class
a = 'hello'
b = 1
c = True
fc = First_class
'''
print(tk.__name__)
print(tkinter.__name__)
print(first_f.__name__)
print(first_c.__name__)
print(first_func.__name__)
print(First_class.__name__)
print(type(a))
print(hasattr(a, 'count'))
print(issubclass(Second_class, First_class))
print(isinstance(fc, First_class))
print(inspect.ismodule(a))
print(inspect.getmodule(tkinter))

print(sys.version)'''
__builtins__