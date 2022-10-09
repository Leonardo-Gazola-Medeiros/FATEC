def checa_numero():
    
    x = 0
    
    for i in range(18644,33088):
        if '7' not in str(i) and '2' in str(i):
            x += 1
    return print(x)
checa_numero()