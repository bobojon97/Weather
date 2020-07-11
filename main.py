from colorama import init
from  colorama import Fore, Style, Back

init()
print(Fore.BLACK)
print(Back.GREEN)

what = input('Выбери  (+, -): ')

print(Back.CYAN)

a = int(input('Первои число  '))

b = int(input('Второе число  '))

print(Back.YELLOW)

if what == '+':
	c = a+b
	print('res', c)
	

elif what == '-':
	c = a-b
	print('res', c)


else:
	print('Не верная операция')
	
input()
