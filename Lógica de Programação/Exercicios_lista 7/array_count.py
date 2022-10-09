# C. array_count9
# conta quantas vezes aparece o 9 numa lista nums


def array_count9(nums):
  #Creating a variable called nines to store all the 9 into the list.
  nines = 0
  for i in range(len(nums[:])):   
    if nums[i] == 9:
        nines = nines+1
  return nines


