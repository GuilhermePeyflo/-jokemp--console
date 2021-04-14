from Jogo import Jogo


print("\033[1;33m--- Bem vindo ao Pedra, Papel e Tesoura ---\0331;33m]")
while True:
    if Jogo().iniciar_jogo() == "1":
        pass
    else:
        break
