# coding=utf-8
import forca
import adivinhacao
import os

def escolher_jogos():
    print("**********************")
    print("  ESCOLHA O SEU JOGO  ")
    print("**********************")

    print("1 - Jogo da Forca")
    print("2 - Jogo de Adivinhação")

    # Running in...
    run = os.getenv("RUNIN")
    if run == "docker":
        jogo = int(os.getenv("GAME"))
        print("Digite o numero do jogo: ", jogo)
    else:
        jogo = int(input("Digite o numero do jogo: "))

    if jogo == 1:
        print("Jogo da Forca")
        forca.jogar()
    elif jogo == 2:
        print("Jogo da Adivinhação")
        adivinhacao.jogar()

if __name__ == "__main__":
    escolher_jogos()
