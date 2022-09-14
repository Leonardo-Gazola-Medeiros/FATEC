import random

lista = [x for x in range(1,101)]

sorteados = []

while 20 > len(sorteados):
    sorteados.append(random.choice(lista))

pares = [x for x in sorteados if x%2 == 0]
impares = [x for x in sorteados if x%2 != 0]

print('Os numeros sorteados foram: ', sorteados)
print('Dentre estes numeros, os numeros pares são: ', pares)
print('E os numeros impares são: ',impares)
