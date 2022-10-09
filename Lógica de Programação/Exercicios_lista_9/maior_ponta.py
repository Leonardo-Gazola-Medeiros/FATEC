# D. maior_ponta #
# Dada uma lista não vazia, cria uma nova lista onde todos
# os elementos são o maior das duas pontas
# obs.: não é o maior de todos, mas entre as duas pontas
# maior_ponta([1, 2, 3]) -> [3, 3, 3]
# maior_ponta([1, 3, 2]) -> [2, 2, 2]


def maior_ponta(nums):
    
    
    #DEFININDO O MAIOR NUMERO DAS PONTAS
    if nums[0] >= nums[-1]:
        maior = nums[0]
    else:
        maior = nums[-1]
    
    
    #ADICIONANDO O MAIOR VALOR EM UMA NOVA LISTA DE MESMA LEN Q A ORIGINAL
    
    contador = 0
    final = []
    while contador < len(nums[:]):
        final.append(maior)
        contador = contador + 1
    
    return (final[:])