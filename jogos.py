from forca import forca
from adivinhação import adivinhação

def escolhe_jogo():
    print('*************************************')
    print('********* Escolha seu Jogo! *********')
    print('*************************************')

    print('Lista de Jogos: \n'
          '1 - Forca! \n'
          '2 - Adivinhação!')

    jogo = int(input('Escolha o jogo: '))

    if (jogo == 1):
        print('Jogar forca!')
        forca.jogar()
    elif (jogo == 2):
        print('Jogo adiivnhação')
        adivinhação.jogar()

if(__name__ == '__main__'):
    escolhe_jogo()