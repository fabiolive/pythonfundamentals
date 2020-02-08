#laço de repetição

# frutas =['abacaxi','banana','caju']
# t = enumerate(frutas)

# for i,f in t:
#     if f == 'banana':
#         print(i,f)





# for i in frutas
#     print(i)

# carros = ('golf','camaro','fusca')

# for carro in carros:
#     print(carro)


# itens = []

# for item in range(1,100):
#     itens.append(item)
# print(itens)

# carros = ['golf','fox','camaro']
# cores = ['branco', 'preto', 'azul']
# for carro in carros:
#     for cor in cores:
#         print(carro, cor)



# for i in range(1, 50000000):
#     print(i)
#     if i == 50:
#         continue


# try:
# 	if nome == 'Retano':
# 		print(nome)

# except Exception as e:
# 	print('Erro variavel não existe!!')

# while True:
#     try:
#         x = int(input("Digite o primeiro valor: "))
#         y = int(input("Digite o segundo valor: "))
#         print(x + y)
#         break
#     except ValueError:
#         print('digite apenas números ')



# #finally

# try:
#     x = int(input("Digite o primeiro valor: "))
#     y = int(input("Digite o segundo valor: "))
#     print(x + y)
#     break
# except ValueError:
#     print('digite apenas números ')

# finally:
#     print('Saindo do try/exept')




# blacklist = ['daniel','camila']
# try:
#     nome = input('Digite o seu nome: ')
#     print(nome)
#     if nome in blacklist:
#         raise NameError('Usuário bloqueado')
# except NameError as n:
#     print(n)

# abrindo arquivos!!!


#COMANDO 'whith open '

# with open ('Arquivo.txt', 'a') as f:
#     f.seek(0)   
#     f.write('Curso de Python')

with open ('Arquivo.txt', 'r') as f:
    print(f.read())
    f.seek(0)
    print(f.read())
    f.close()

