usuario = str(input('Digite o nome de usuario: '))
senha = str(input('Digite a senha: '))

while senha == usuario:
    print('Não é possível o nome de usuário e a senha serem iguais')
    usuario = str(input('Redefina o nome de usuário: '))
    senha = str(input('Redefina a senha: '))
print('Cadastro realizado com sucesso.')