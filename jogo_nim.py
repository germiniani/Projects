"""
Jogo do NIM!
Desenvolvido por m1mir
Exercício de Python idealizado pela USP no curso de introdução à ciencia da computação com Python parte 1
"""

import random


def computador_escolhe_jogada(n, m):
    # Essa função escolhe a melhor jogada possível para o computador
    jc = 0
    if n % (m + 1) == 0:
        jc = random.randrange(1, m + 1)
    elif n == m:
        jc = m
    else:
        while n % (m + 1) != 0:
            n -= 1
            jc += 1

    return jc


def usuario_escolhe_jogada(m):
    # Essa função define a jogada do usuário
    ju = int(input("Quantas peças você vai tirar? "))
    while ju > m or ju <= 0:
        print("Oops! Jogada inválida! Tente de novo.")
        print()
        ju = int(input("Quantas peças você vai tirar? "))
    return ju


def partida():
    # Essa função gera uma partida
    v = 0
    vitoria = False
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    print()
    primeira_jogada = n % (m + 1)
    if primeira_jogada == 0:
        print("Você começa!")
        print()
        while not vitoria:
            ju = usuario_escolhe_jogada(m)
            n -= ju
            if ju > 1:
                print("Você tirou", ju, "peças.")
            else:
                print("Você tirou uma peça.")

            if n == 1:
                print("Agora resta apenas uma peça no tabuleiro.")
            else:
                if n > 1:
                    print("Agora restam", n, "peças no tabuleiro.")
                else:
                    if n == 0:
                        print("Fim do jogo! Você ganhou!")
                        vitoria = True
                        v = 1
            print()
            if n > 0:
                jc = computador_escolhe_jogada(n, m)
                n -= jc
                if jc > 1:
                    print("O computador tirou", jc, "peças.")
                else:
                    print("O computador tirou uma peça.")

                if n == 1:
                    print("Agora resta apenas uma peça no tabuleiro.")
                else:
                    if n > 1:
                        print("Agora restam", n, "peças no tabuleiro.")
                    else:
                        if n == 0:
                            print("Fim do jogo! O computador ganhou!")
                            vitoria = True
                            v = 2
                print()
    else:
        print("Computador começa!")
        print()
        while not vitoria:
            jc = computador_escolhe_jogada(n, m)
            n -= jc
            if jc > 1:
                print("O computador tirou", jc, "peças.")
            else:
                print("O computador tirou uma peça.")

            if n == 1:
                print("Agora resta apenas uma peça no tabuleiro.")
            else:
                if n > 1:
                    print("Agora restam", n, "peças no tabuleiro.")
                else:
                    if n == 0:
                        print("Fim do jogo! O computador ganhou!")
                        vitoria = True
                        v = 2
            print()
            if n > 0:
                ju = usuario_escolhe_jogada(m)
                n -= ju
                if ju > 1:
                    print("Você tirou", ju, "peças.")
                else:
                    print("Você tirou uma peça.")

                if n == 1:
                    print("Agora resta apenas uma peça no tabuleiro.")
                else:
                    if n > 1:
                        print("Agora restam", n, "peças no tabuleiro.")
                    else:
                        if n == 0:
                            print("Fim do jogo! Você ganhou!")
                            vitoria = True
                            v = 1
                print()
    return v


def campeonato():
    pontos_usuario = 0
    pontos_computador = 0
    print()
    print("**** Rodada 1 ****")
    print()
    pontos = partida()
    if pontos == 1:
        pontos_usuario += 1
    else:
        pontos_computador += 1
    print("**** Rodada 2 ****")
    print()
    pontos = partida()
    if pontos == 1:
        pontos_usuario += 1
    else:
        pontos_computador += 1
    print("**** Rodada 3 ****")
    print()
    pontos = partida()
    if pontos == 1:
        pontos_usuario += 1
    else:
        pontos_computador += 1

    print("**** Final do Campeonato ****")
    print()
    print("Placar: Você", pontos_usuario, "X", pontos_computador, "Computador")
    return 0


print("Bem-vindo ao jogo do NIM!")
print()
regras = int(input("Você deseja ver as regras do jogo primeiro?\n0 - para sim\n1 - para não "))
if regras == 0:
    print("\nRegras:\nHaverão uma certa quantidade de peças no jogo, definidas por você."
          + "\nA ideia é ir tirando tantas peças do jogo,"
          + " alternando as jogadas entre você e o computador, até que o jogador que tirar a ultima(s) peça(s) ganha."
          + "\nPorém, existe um limite de peças que podem ser tiradas por jogada,"
          + " esse limite também é definido por você.")
print()
print("Escolha:")
print("1 - para jogar uma partida isolada")
c = int(input("2 - para jogar um campeonato "))
if c == 1:
    print()
    print("Você escolheu uma partida isolada!")
    print()
    partida()
if c == 2:
    print()
    print("Você escolheu um campeonato!")
    campeonato()
