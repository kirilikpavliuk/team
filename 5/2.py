from colorama import init, Fore#функції для виводу тексту в консоль
from colorama import Back#функції для виводу тексту в консоль
from colorama import Style #функції для виводу тексту в консоль

init(autoreset=True)# підтримка виводу на Windows 10

print(Fore.BLUE + 'hello world') # робить текст заданого кольору
print(Back.WHITE + 'hello world')#робить фон тексту заданим кольором
print(Style.BRIGHT + 'hello world')#робить текст курсивом
print(Style.RESET_ALL)# робить пробіл у тексті
print('hello world')#просто текст
