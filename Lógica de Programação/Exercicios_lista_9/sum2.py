# E. sum2 #
# Dada uma lista de inteiros de qualquer tamanho
# retorna a soma dos dois primeiros elementos
# se a lista tiver menos de dois elementos, soma o que for possível


def sum2(nums):
    
    if len(nums) >= 2:
        return (nums[0]+nums[1])
    elif len(nums) == 1:
        return (nums[0])
    else:
        return 0