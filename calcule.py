red, WHITE, CYAN, GREEN, DEFAULT = '\033[91m', '\033[46m', '\033[36m', '\033[1;32m',  '\033[0m'

print(WHITE,'========== Welcome to Calculater ==========               ')

print('1:go to calcule    2:hellp    3:exit')

h = input('Enter your choice==> ')
if h == '2' : 
    print('helped')
    print('go to calcule now')
if h == '3' : print('',DEFAULT), exit()
    
x_1 = int(input('Enter first number ===> '))
t = input('Enter type math===> ')
x_2 = int(input('Enter second number==> '))

if t == '+':print(GREEN,'{} + {}=' .format(x_1, x_2))
if t == '+':print(GREEN,x_1 + x_2)

if t == '-':print(GREEN,'{} - {}=' .format(x_1, x_2))
if t == '-':print(GREEN,x_1 - x_2)

if t == '*':print(GREEN,'{} * {}=' .format(x_1, x_2))
if t == '*':print(GREEN,x_1 * x_2)

if t == '/':print(GREEN,'{} / {}=' .format(x_1, x_2))
if t == '/':print(GREEN,x_1 / x_2)

if x_1 > x_2 :print(GREEN,x_1,'>',x_2)
if x_1 < x_1 :print(GREEN,x_1,'<', x_2,DEFAULT)
print('',DEFAULT)



