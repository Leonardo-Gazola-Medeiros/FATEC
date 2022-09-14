area = float(input('Tamanho da área em m² = '))
latas = int(area/(18*3))

if area%(18*3) != 0:
    latas = latas + 1

print(f'Para cobrir esta área de {area:.2f}m², serão necessárias {latas:.2f} latas de tinta, o que irá custar {latas*80:.2f}R$')


    


