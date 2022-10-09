# A. first_last6
# verifica se 6 é o primeiro ou último elemento da lista nums
# first_last6([1, 2, 6]) -> True
# first_last6([6, 1, 2, 3]) -> True
# first_last6([3, 2, 1]) -> False


def first_last6(nums): 
    
    if (nums[0] == 6) or (nums[-1] == 6):
        return True
    else:
        return False