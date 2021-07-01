# Simulador de Dado
# Simular o uso de um dado, gerando um valor de 1 até 6
import random

class Simuladordedado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado?'

    def iniciar(self):
        resposta = input(self.mensagem)
        if resposta == 'sim':
            self.GerarValorDoDado()
    

    def GerarValrDoDado(self):
        