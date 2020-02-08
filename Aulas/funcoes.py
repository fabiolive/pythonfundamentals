# -*- coding: utf-8 -*-
 
# produtos = []
# novos_pridutos = ['calça','meia']
# def cadastraProduto(produto):
#     global produtos
#     produtos.append(produto)

# cadastraProduto('batata')

# def cadastraProduto(produto):
#     global produtos
#     produtos.append(produto)

# cadastraProduto('laranja')


# print(produtos)

# def deletarProduto(produto):
#     global produtos
#     produtos.remove(produto)

# def listarProdutos(lista=produtos):
#     global produtos
#     print(lista)

# cadastraProduto('laranja')
# cadastraProduto('laranja')
# cadastraProduto('laranja')
# deletarProduto('laranja')
# listarProdutos(novos_pridutos)

# def subtracao(x,y):
#     print('Total subtracao:',x - y)

# def soma(x,y):
#     print('Total soma: ',x + y)

# def soma(x,y):
#     return x + y

# def sub(x,y):
#     return x-y


# print(soma(10,5))
# print(sub(15,5))

# def maior(x,y):
#     if x > y:
#         print(x)
#     else:
#         print(y)

# maior(100,5)

# args


# def maior(*valores):
#     print(max(valores))


# maior(1,2,3,5,3,5,56,3,5,5,)


# t = dict(key='valor',key2='valor 2)
# import requests

# def api(**valores):
#     req = requests.get(valores['URL'])
#     print(valores)
#     return req


# print(api(URL='https://www.google.com', code_status='valor_esperado_200', retorno='OK'))




#FUNÇÃO LAMBIDA

lista = [1,2,4,5,6,7,8,9]

dobro = list(map(lambda x : x*2,lista))
print(dobro)


