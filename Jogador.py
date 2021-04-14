from Usuario import Usuario


class Jogador(Usuario):
    def __init__(self):
        while True:
            self.nome = input("Nome do Jogador: ")
            if self.nome == "":
                pass
            else:
                break
        self.cartas_atuais = []

    def selecionar_carta(self):
        while True:
            try:
                carta = input("Selecione a carta que deseja jogar: ")
                self.carta_selecionada = self.cartas_atuais[int(carta) - 1]
                self.cartas_atuais.pop(int(carta) - 1)
                break
            except:
                print("Esta carta não está na sua mão")
        return True
