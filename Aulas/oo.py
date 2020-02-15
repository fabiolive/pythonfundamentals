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
def addArmazenamento(self, adda):
    self.disco += adda
def mudaSevico(self, muda):
    self.servico += muda


servidorWeb = Servidor('Nginx',250,'I7 9 Gereção',16)
adm = int(input('Digite a quandidade de mempria a armazenar'))
print(servidorWeb.memoria(adm))


