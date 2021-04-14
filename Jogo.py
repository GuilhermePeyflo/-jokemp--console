import random
from Computador import Computador
from Jogador import Jogador


class Jogo:
    numeros = []

    def distribuir_cartas(self, jogador):
        self.numeros.clear()
        for i in range(3):
            self.numeros.append(random.randint(1, 3))
        for n in self.numeros:
            if n == 1:
                jogador.cartas_atuais.append("Pedra")
            elif n == 2:
                jogador.cartas_atuais.append("Tesoura")
            elif n == 3:
                jogador.cartas_atuais.append("Papel")

    def carta_vencedora(self, carta_j1, carta_j2):
        if carta_j1 == carta_j2:
            return "Empate"
        elif carta_j1 == "Pedra" and carta_j2 != "Papel":
            return "Jogador 1"
        elif carta_j1 == "Papel" and carta_j2 != "Tesoura":
            return "Jogador 1"
        elif carta_j1 == "Tesoura" and carta_j2 != "Pedra":
            return "Jogador 1"
        else:
            return "Jogador 2"


    def jogo_pvp(self):

        print("Jogador 1")
        jogador1 = Jogador()

        print("Jogador 2")
        jogador2 = Jogador()

        rodada = 1
        self.distribuir_cartas(jogador1)
        self.distribuir_cartas(jogador2)
        print("CARTAS DISTRIBUIDAS !!")
        while True:
            print(f"Rodada {rodada} de 3\n")

            print("Vez do jogador 1")
            input("Pressione Qualquer tecla para ver suas cartas ...\n")
            jogador1.ver_cartas()
            jogador1.selecionar_carta()

            print("Vez do jogador 2")
            input("Pressione Qualquer tecla para ver suas cartas ...\n")
            jogador2.ver_cartas()
            jogador2.selecionar_carta()

            if Jogo().carta_vencedora(jogador1.carta_selecionada, jogador2.carta_selecionada) == "Jogador 1":
                print(f"O jogador {jogador1.nome} Venceu !!")
                break
            elif Jogo().carta_vencedora(jogador1.carta_selecionada, jogador2.carta_selecionada) == "Jogador 2":
                print(f"O jogador {jogador2.nome} Venceu !!")
                break
            else:
                print(f"Empate, os dois jogaram {jogador1.carta_selecionada}\n")
            rodada += 1
            if rodada == 4:
                print(f"A partida terminou empatada")
                break
        print("-" * 100)
        print("Fim do Jogo\n")

    def jogo_pvc(self):
        print("Jogador 1")
        jogador1 = Jogador()

        computador = Computador()

        rodada = 1
        self.distribuir_cartas(jogador1)
        self.distribuir_cartas(computador)
        print("CARTAS DISTRIBUIDAS !!")
        while True:
            print(f"Rodada {rodada} de 3\n")

            print("Vez do jogador 1")
            input("Pressione Qualquer tecla para ver suas cartas ...\n")
            jogador1.ver_cartas()
            jogador1.selecionar_carta()

            print("Vez do Computador")
            input("Pressione Qualquer tecla para o computador jogar ...\n")
            computador.ver_cartas()
            print(f"O computador escolheu {computador.selecionar_carta()}")

            if Jogo().carta_vencedora(jogador1.carta_selecionada, computador.carta_selecionada) == "Jogador 1":
                print(f"O jogador {jogador1.nome} Venceu !!")
                break
            elif Jogo().carta_vencedora(jogador1.carta_selecionada, computador.carta_selecionada) == "Jogador 2":
                print(f"O {computador.nome} Venceu !!")
                break
            else:
                print(f"Empate, os dois jogaram {jogador1.carta_selecionada}\n")
            rodada += 1
            if rodada == 4:
                print(f"A partida terminou empatada")
                break
        print("-" * 100)
        print("Fim do Jogo\n")

    def iniciar_jogo(self):
        tipo_jogo = input("\nEscolha contra quem jogar\n 1) Jogador\n 2) Computador\n")
        try:
            if tipo_jogo == "1":
                self.jogo_pvp()
            elif tipo_jogo == "2":
                self.jogo_pvc()
            return input("Deseja jogar novamente? \n1) Sim\n2) Não\n")
        except:
            print("Opção inválida")


