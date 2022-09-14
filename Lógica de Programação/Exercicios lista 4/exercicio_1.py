import random

lista = [x for x in range(1,101)]

sorteados = []

while 10 > len(sorteados):
    sorteados.append(random.choice(lista))

print('Os numeros sorteados foram: ', sorteados)
sorteados.sort()
print('Dentre os quais, o maior valor destes é: ', sorteados[9] , ' , e o menor é: ', sorteados[0])
