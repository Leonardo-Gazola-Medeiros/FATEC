import random

sorteados_1 = []
sorteados_2 = []
primeiros = random.sample(range(100),10)
segundos = random.sample(range(100),10)

sorteados_1.append(primeiros)
sorteados_2.append(segundos)

lista_final = []

for a , b in zip(primeiros,segundos):
    lista_final.append(a)
    lista_final.append(b)

print('Os valores presentes no primeiro vetor são: ', sorteados_1)
print('Os valores do segundo vetor são: ', sorteados_2)
print('A junção destes dois vetores resulta num vetor final com os seguintes valores: ', lista_final)