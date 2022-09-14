num1 = 1
num2 = 1
fib = 0
x = 1
sequencia = int(input('Digite o elemento que deseja da sequencia: '))

while x < 3:
    x = x+1
    print('1')

while x <= sequencia:
    fib = num1 + num2
    num1 = num2
    num2 = fib
    print(fib)
    x = x+1
