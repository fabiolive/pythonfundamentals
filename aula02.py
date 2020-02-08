
#MÉTODOS////////////
# texto = 'isso é um texto'

# texto.upper()
# texto.lower()
# texto.capitalize()
# print(texto.split(" "))

#LISTA/////////////

# lista = ['abacaxi', 'carro', 'navio',15,5.5]

# lista.append('vl')
# lista.pop(0)
# lista.remove()
# print(lista[3])


# #TUPLAS////

# valores = ( 1,2 )

# print(type(valores))


#DICIONÁRIO

# ling_favorita = {'joao':'Java','Daniel':'Python','Hector':'PHP'}
# print(ling_favorita['Daniel'])

#time_favorito = {'Joao':'Corithians','Rafael':'Vasco','Camila':'Palmeiras',}
#print(time_favorito['Camila'])

#time_favorito['Rafael'] = 'Flamengo'
# print(time_favorito)
# print(time_favorito.values)
# print(time_favorito.keys)

dados_clientes = {'cliente': {'cl001': {'nome': 'Rafael da silva','idade': 25,'telefone': '011954243647'},
                              'cl002': {'nome': 'Carla Pereira','idade': 28,'telefone': ''}}}

#print(dados_clientes)
#print(dados_clientes['cliente']['cl002']['nome'], dados_clientes)
# dados_clientes['cliente']['cl002']['telefone'] = '11958555447'
# print(dados_clientes)

imprime_clientes = input('Digite o codigo do cliente : ')
print(dados_clientes['cliente'][imprime_clientes])




