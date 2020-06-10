import random


def jogar():
    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):
        chute = insere_chute()

        if (chute in palavra_secreta):
            marca_acerto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            print(f'Ops, voce errou! Faltam {7 - erros} tentativas.')
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        mostra_mensagem_vencedor()
    else:
        mostra_mensagem_perdedor(palavra_secreta)


def imprime_mensagem_abertura():
    print('*************************************')
    print('*****Bem vindo ao jogo de Forca!*****')
    print('*************************************')


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ['_' for letra in palavra]


def insere_chute():
    chute = input('Insira sua letra: ')
    chute = chute.strip().upper()
    return chute


def marca_acerto(chute, letras_acertadas, palavra_secreta):
    i = 0
    for letra in palavra_secreta:
        if (chute == letra.upper()):
            letras_acertadas[i] = letra
        i += 1


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def mostra_mensagem_vencedor():
    print('Parabéns! Você ganhou!')
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def mostra_mensagem_perdedor(palavra_secreta):
    print(f'MORREU! \n'
          f'A palavra secreta era {palavra_secreta}!')
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|    XX       XX    | /   ")
    print(" |   X  X     X  X   |/     ")
    print(" |    XX       XX    |      ")
    print(" |         x         |      ")
    print(" \__       X       __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I         I  |        ")
    print("   \    I I I I  _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


if __name__ == '__main__':
    jogar()
