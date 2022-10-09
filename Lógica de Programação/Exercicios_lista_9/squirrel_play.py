# H. squirrel_play
# os esquilos na FATEC brincam quando a temperatura está entre 60 e 90
# graus Fahreneit (são estrangeiros e o termômetro é diferente rs)
# caso seja verão, então a temperatura superior é 100 no lugar de 90
# retorne True caso os esquilos brinquem
# squirrel_play(70, False) -> True
# squirrel_play(95, False) -> False
# squirrel_play(95, True) -> True


def squirrel_play(temp, is_summer):

    if is_summer == True:
        if temp in range(60,101):
            return True
        else:
            return False
    else:
        if temp in range(60,91):
            return True
        else:
            return False