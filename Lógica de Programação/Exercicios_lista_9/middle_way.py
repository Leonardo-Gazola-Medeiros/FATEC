# F. middle_way #
# sejam duas listas de inteiros a e b
# retorna uma lista de tamanho 2 contendo os elementos do
# meio de a e b, suponha que as listas tem tamanho ímpar
# middle_way([1, 2, 3], [4, 5, 6]) -> [2, 5]
# middle_way([7, 7, 7], [3, 8, 0]) -> [7, 8]
# middle_way([5, 2, 9], [1, 4, 5]) -> [2, 4]


def middle_way(a, b):
    
    final_res = []
    
    
    final_res.append( a[((len(a)))//2] )
    final_res.append( b[((len(b)))//2] )
    
    return final_res
