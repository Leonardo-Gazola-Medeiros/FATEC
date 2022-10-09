# J. roda2
# rodar uma string s duas posições
# a string possui pelo menos 2 caracteres
# left2('Hello') -> 'lloHe'
# left2('Hi') -> 'Hi'

def roda2(s):
  
  return ((s[2:])+(s[0])+(s[1]))

print(roda2('python'))

