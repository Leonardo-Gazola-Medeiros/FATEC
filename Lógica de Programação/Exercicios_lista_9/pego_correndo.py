# I. pego_correndo
# você foi pego correndo
# o resultado será:
# sem multa = 0
# multa média = 1
# multa grave = 2
# velocidade <= 60 sem multa
# velocidade entre 61 e 80 multa média
# velocidade maior que 81 multa grave (cidade do interior)
# caso seja seu aniversário a velocidade pode ser 5 km/h maior em todos os casos
# pego_correndo(60, False) -> 0
# pego_correndo(65, False) -> 1
# pego_correndo(65, True) -> 0 


def pego_correndo(speed, is_birthday):
  
  if is_birthday == True:
    if speed <= 65:
      return 0
    if speed in range(66,86):
      return 1
    if speed > 86:
      return 2
  else:
    if speed <= 60:
      return 0
    if speed in range(61,81):
      return 1
    if speed > 81:
      return 2
        