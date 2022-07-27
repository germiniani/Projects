import os


def forca():
    palavra = input("Palavra chave: ")
    resultado = False
    tentativas = []
    chances = 7
    tamanho = len(palavra)
    acertos = []
    while tamanho > 0:
        acertos += '_'
        tamanho -= 1

    while True:
        os.system("clear")
        print(f'Você tem {chances} tentativas')
        if chances < 7:
            print('Letras já tentadas: ')
            for a in tentativas:
                print(f'{a},', end='')
            print('')
        print('\nacertos:')
        for g in acertos:
            print(f'{g} ', end='')
        print('')
        letra = input("tente uma letra: ")
        if len(letra) > 1:
            print('Tentativa inválida!')
        elif letra in palavra:
            num = 0
            for l in palavra:
                if l == letra:
                    acertos[num] = letra
                num += 1
            if '_' not in acertos:
                resultado = True
                break
        elif letra in tentativas:
            pass
        else:
            if chances > 1:
                chances -= 1
                tentativas += letra
            else:
                print('Você perdeu')
                break

    if resultado:
        print('Parabéns!')
    else:
        print('Acertos: ', end='')
        for g in acertos:
            print(g, end=' ')
    print(f'Resposta: {palavra}')
    fim = input('fim de jogo!')


def main():
    while True:
        os.system("clear")
        inicio = input("Aperte 'Enter' para começar")
        if inicio == "":
            forca()
        else:
            break

if __name__ == "__main__":
    main()
