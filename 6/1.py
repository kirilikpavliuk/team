def sum_numbers (num1, num2, num3):
    try:
        num1 = int(num1)
        num2 = int(num2)
        num3 = int(num3)
        res = num1 + num2 + num3
        print(res)
    except ValueError:
        print( 'Ви ввели не число')
    except ZeroDivisionError:
        print ('Na 0 dilitu ne mozna')
    except Exception as xcs:
        print(xcs)
    else:
        print('Else')
n_1 = input('Введіть число 1: ')
n_2 = input('Введіть число 2: ')
n_3 = input('Введіть число 3: ')
print(sum_numbers(n_1, n_2, n_3))