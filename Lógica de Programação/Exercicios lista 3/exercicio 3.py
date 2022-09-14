pop_1 = float(input('Total da população A: '))
k1 = float(input('Coeficiente de crescimento de A%: '))
pop_2 = float(input('Total da população B: '))
k2 = float(input('Coeficiente de crescimento de B: '))
anos = 0


while pop_1 < pop_2:
    pop_1 = (pop_1 + ((k1/100)*pop_1))
    pop_2 = (pop_2 + ((k2/100)*pop_2))
    anos = anos + 1
pop_1 = int(pop_1)
pop_2 = int(pop_2)
print(f'As duas populações em questão terão o mesmo número de indivíduos após {anos:.2f} anos')
print(f'Quando a população A alcançar {pop_1:.2f} indivíduos e a população B tiver {pop_2:.2f}')

