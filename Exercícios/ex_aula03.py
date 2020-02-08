# faça um sistema de login

# usuarios = ['Caio', 'Felipe', 'Manuela', 'Paula', 'Daniel', 'Camila']

# se o usuario digitado estiver na lista de usuarios
#   imprima acesso permitido

# se não
#    imprima acesso negado
#    e peça para digitar o usuario novamente



usuarios = ['Caio', 'Felipe', 'Manuela', 'Paula', 'Daniel', 'Camila']


while True:
    try:
        nome = input('Digite o nome do usuário: ')

        if nome not in usuarios:
            raise NameError('usuário não cadastrado!! Digite Npvamente')
            continue
        else:
            print('Acesso permitido!!')
            break
    except NameError as n:
        print(n)



