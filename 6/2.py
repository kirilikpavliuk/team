class MyException():
    def __str__(self):
        return 'Exception, yopta'

def sum_numbers(num1, num2, num3):
    if not num2.isdigit() or not num1.isdigit() or not num3.isdigit():
        raise ValueError

n_1 = input('Введіть число 1: ')
n_2 = input('Введіть число 2: ')
n_3 = input('Введіть число 3: ')
