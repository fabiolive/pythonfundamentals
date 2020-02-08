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



#finally

try:
    x = int(input("Digite o primeiro valor: "))
    y = int(input("Digite o segundo valor: "))
    print(x + y)
    break
except ValueError:
    print('digite apenas números ')

finally:
    print('Saindo do try/exept')