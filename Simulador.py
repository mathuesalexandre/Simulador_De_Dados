from random import randint
import PySimpleGUI as sg

class SimuladorDeDados:
    def __init__(self):
        self.minimo = 1
        self.maximo = 6
        self.mensagem = 'Você quer rodar o dado? '
        #layout
        self.layout = [[sg.Text('Jogar o dado?')],
                       [sg.Button('Sim'), sg.Button('Não')]
                        ]


    def iniciar(self):
        #criar uma janela
        self.janela = sg.Window('Simulador de Dado', layout=self.layout)
        #ler os valores da tela
        self.eventos, self.valores =self.janela.Read()
        try:
            if self.eventos[0] == 'S':
                self.gerarValorDoDado()
            elif self.eventos[0] == 'N':
                print('Tudo bem, obrigado pelo seu tempo.')
            else:
                 print('Digite apenas sim ou não.')
        except:
            print('Ocorreu um ERRO!')


    def gerarValorDoDado(self):
        print(randint(self.minimo, self.maximo))

simulador = SimuladorDeDados()
simulador.iniciar()