num = int(input('digite um numero de 0 a 10: '))

while (0<= num <=10) is False :
    print('o valor digitado é invalido')
    num = int(input('digite outro valor no intervalo entre 1 e 10: '))
print(f'o numero escolhido {num:.2f} é válido.')