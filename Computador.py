import random
from Usuario import Usuario


class Computador(Usuario):
    def __init__(self):
        self.nome = "CPU"
        self.cartas_atuais = []

    def selecionar_carta(self):
        self.carta_selecionada = random.choice(self.cartas_atuais)
        self.cartas_atuais.remove(self.carta_selecionada)
        return self.carta_selecionada
