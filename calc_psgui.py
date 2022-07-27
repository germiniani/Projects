"""
Calculadora composta com interface gráfica.
Criada por Gustavo Germiniani
"""

import PySimpleGUI as sg  # Framework de interfaces gráficas


def calcula(conta):  # Calcula o que foi passado para a calculadora
    try:
        conta = conta.split()
        while '*' in conta or '/' in conta:
            i = 0
            while i < len(conta):
                if conta[i] in ('*', '/'):
                    if i + 1 == len(conta) or conta.index(conta[i - 1]) == len(conta) - 1:
                        conta.pop(i)
                    else:
                        if conta[i] == '*':
                            conta[i - 1] = float(conta[i - 1]) * float(conta[i + 1])
                        else:
                            conta[i - 1] = float(conta[i - 1]) / float(conta[i + 1])
                        conta.pop(i + 1)
                        conta.pop(i)
                        break
                i += 1
        if len(conta) > 1:
            while '+' in conta or '-' in conta:
                i = 0
                while i < len(conta):
                    if conta[i] in ('+', '-'):
                        if i + 1 == len(conta) or conta.index(conta[i - 1]) == len(conta) - 1:
                            conta.pop(i)
                        else:
                            if conta[i] == '+':
                                conta[i - 1] = float(conta[i - 1]) + float(conta[i + 1])
                            else:
                                conta[i - 1] = float(conta[i - 1]) - float(conta[i + 1])
                            conta.pop(i + 1)
                            conta.pop(i)
                            break
                    i += 1
        j = str(conta[0])
        j = j.split('.')
        if j[1] == '0':
            return j[0]
        else:
            return str(conta[0])
    except:
        return 'Erro'


sg.ChangeLookAndFeel('SystemDefault')  # Tema da calculadora
size = (7, 2)
layout = [
    [sg.Output(size=(40, 8), k='Output')],
    [sg.Button('1', k='1', size=size), sg.Button('2', k='2', size=size), sg.Button('3', k='3', size=size),
     sg.Button('+', k='+', size=size)],
    [sg.Button('4', k='4', size=size), sg.Button('5', k='5', size=size), sg.Button('6', k='6', size=size),
     sg.Button('-', k='-', size=size)],
    [sg.Button('7', k='7', size=size), sg.Button('8', k='8', size=size), sg.Button('9', k='9', size=size),
     sg.Button('*', k='*', size=size)],
    [sg.Button('.', k='.', size=size), sg.Button('0', k='0', size=size), sg.Button('=', k='=', size=size),
     sg.Button('/', k='/', size=size)],
]

tela = sg.Window('Calculadora', layout=layout, margins=(0, 0), font=('arial', '15'), auto_size_text=True,
                 auto_size_buttons=True, grab_anywhere=True, icon='Calculator_30001.ico')
ult_result = conta = ''

while True:  # Analisa todas as entradas do usuário
    event, values = tela.read()
    if event in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        if ult_result == conta:
            ult_result = conta = ''
        conta += event
        print(event, end='')
    elif event in ('+', '-', '*', '/'):
        if conta != '' and ult_result != '':
            print(conta, end='')
            ult_result = ''
        conta += f' {event} '
        print(f' {event} ', end='')
    elif event == '.':
        if conta[-1] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            conta += event
            print(event, end='')
        else:
            pass
    elif event == '=':
        if conta == ult_result:
            print(conta)
        else:
            conta = calcula(conta)
            ult_result = conta
            print(f' = {ult_result}')
    else:
        tela.close()
        break
