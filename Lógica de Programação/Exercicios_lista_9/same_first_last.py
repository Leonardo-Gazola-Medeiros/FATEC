# B. same_first_last #
# retorna True se a lista nums
# possui pelo menos um elemento
# e o primeiro elemento é igual
# ao último
# same_first_last([1, 2, 3]) -> False
# same_first_last([1, 2, 3, 1]) -> True
# same_first_last([1, 2, 1]) -> True


def same_first_last(nums):
    
    if len(nums) == 1:
        return True
    elif len(nums) < 1:
        return False
    elif (nums[0] == nums[-1]):
        return True
    else:
        return False