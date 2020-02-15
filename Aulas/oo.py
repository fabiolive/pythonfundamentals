# -*- coding: utf-8 -*-

# class Carro:
#     def __init__(self):
#         self.rodas = 4
#         self.montor = True
#     def ligar(self):
#         print('ligando...')


# palio = Carro()
# palio.ligar()

class Servidor():

    def __init__(self, servico, disco, processador, memoria):
        self.servico = servico
        self.disco = disco
        self.processador = processador
        self.memoria = memoria

    def addMemoria(self,addm):
        self.memoria += addm
    def addArmazenamento(self, addd):
        self.disco += addd
    def mudaSevico(self, muda):
        self.servico = muda


servidorWeb = Servidor('Nginx', 250,'I7 9 Gereção', 16)

servidorWeb.addMemoria(10)
servidorWeb.addArmazenamento(100)
servidorWeb.mudaSevico('firefox')
print(servidorWeb.memoria)
print(servidorWeb.disco)
print(servidorWeb.servico)



import os.