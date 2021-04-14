class Usuario:
    nome = ""
    carta_selecionada = ""
    pontos_rodada = 0

    def __init__(self):
        self.nome = input("Nome do Jogador: ")
        self.cartas_atuais = []

    def ver_cartas(self):
        for c in range(len(self.cartas_atuais)):
            print(f"{c + 1}) {self.cartas_atuais[c]}")

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
