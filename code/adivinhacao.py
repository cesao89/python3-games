# coding=utf-8
import random


def jogar():
    print("***************************************")
    print("  Olá, Bem vindo ao jogo de advinhação ")
    print("***************************************")

    numero_secreto = random.randrange(1, 101)
    total_tentativas = 0
    pontos = 1000

    print("Escolha o numero de dificuldade:")
    print("1 - Nível Fácil")
    print("2 - Nível Médio")
    print("3 - Nível Díficil")

    nivel = int(input("Definir nível: "))

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        chute = int(chute_str)
        print("Você digitou", chute)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        chute_maior = chute > numero_secreto
        chute_menor = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (chute_maior):
                print("Você erro: seu chute foi maior que o esperado!")
            elif(chute_menor):
                print("Você erro: seu chute foi menor que o esperado!")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Numero Secréto é {}".format(numero_secreto))

    print("***************************************")
    print("              FIM DO JOGO              ")
    print("***************************************")

if(__name__ == "__main__"):
    jogar()
