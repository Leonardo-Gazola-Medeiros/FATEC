dinheiro = float(input('Valor ganho a hora = '))
horas = float(input('Total de horas trabalhadas = '))
sal = dinheiro*horas
leao = sal*0.11
inss = sal*0.08
sindicato = sal*0.05
liquido = sal - leao - inss - sindicato


print(f'O seu salário bruto era de {sal:.2f}R$')
print(f'{leao:.2f}R$ foram para o leão da receita')
print(f'{inss:.2f}R$ foram para o inss')
print(f'{sindicato:.2f}R$ foram o sindicato')
print(f'Por fim, o que restou de seu salário para você foram {liquido:.2f}R$')
