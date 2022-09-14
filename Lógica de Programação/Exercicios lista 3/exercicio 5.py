valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

resto = 0

while valor2 != 0:
    resto = valor1 % valor2
    valor1 = valor2
    valor2 = resto
print(f'O máximo divisor comum entre esses dois valores é: {valor1:.2f}')