import math
import PySimpleGUI as sg

sg.ChangeLookAndFeel('SystemDefault')

layout = [
    [sg.Text('Fórmula de Bhaskara:', background_color='White')],
    [sg.Image(r'image.png')],#Adicione uma imagem da fórmula de bhaskara junto a esse programa
    [sg.Text('Digite o valor de A: ', background_color='White'), sg.Input(size=(10, 0), key='na')],
    [sg.Text('Digite o valor de B: ', background_color='White'), sg.Input(size=(10, 0), key='nb')],
    [sg.Text('Digite o valor de C: ', background_color='White'), sg.Input(size=(10, 0), key='nc')],
    [sg.Button('Calcular'), sg.Button('Fechar')],
    [sg.Output(size=(50,20))]
]

tela = sg.Window('Calcula Bhaskara', layout=layout, margins=(10, 10), font=18, background_color='White')


while True:
    event, values = tela.read()
    a, b, c = float(values['na']), float(values['nb']), float(values['nc'])
    delta1 = (b ** 2) - 4 * a * c
    delta2 = math.sqrt(abs(delta1))
    r1, r2, r3 = (-b / (2 * a)), (+delta2 / (2 * a)), (-delta2 / (2 * a))
    if event == 'Calcular':
        if delta1 < 0:
            if r2 < 0 and r3 < 0:
                print(f'As raízes dessa equação são {r1} - {abs(r2)}i e {r1} - {abs(r3)}i')
            elif r2 < 0:
                print(f'As raízes dessa equação são {r1} - {abs(r2)}i e {r1} + {r3}i')
            elif r3 < 0:
                print(f'As raízes dessa equação são {r1} + {r2}i e {r1} - {abs(r3)}i')
            else:
                print(f'As raízes dessa equação são {r1} + {r2}i e {r1} + {r3}i')
        elif delta1 == 0:
            print('A única raiz real dessa equação é', r1 + r2)
        else:
            print(f'As raízes dessa equação são {r1 + r2} e {r1 + r3}')
    else:
        break
    print('-------------------------------------------------------'
          + '----------------------------')

tela.close()
