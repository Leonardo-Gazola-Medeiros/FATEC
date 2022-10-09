# D. array_front9
# verifica se pelo menos um dos quatro primeiros é nove
# array_front9([1, 2, 9, 3, 4]) -> True
# array_front9([1, 2, 3, 4, 9]) -> False
# array_front9([1, 2, 3, 4, 5]) -> False
def array_front9(nums):
    nine = 0
    for numbers in range(nums[0:5]):
        if numbers == 9:
            nine = nine + 1        
    if nine > 0:
        return True
    else:
        return False
