def divisao_par_range():
    
    numeros = 0

    for i in range(1067,3628):
        if (i%2 == 0) and (i%7 == 0):
            numeros += 1
    return print (numeros)
divisao_par_range()