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
            print(f'Ops, voce errou! Faltam {6-erros} tentativas.')

        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
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
    chute =input('Insira sua letra: ')
    chute = chute.strip().upper()
    return chute

def marca_acerto(chute, letras_acertadas, palavra_secreta):
    i = 0
    for letra in palavra_secreta:
        if (chute == letra.upper()):
            letras_acertadas[i] = letra
        i += 1

def mostra_mensagem_vencedor():
    print('Parabéns! Você ganhou!')


def mostra_mensagem_perdedor(palavra_secreta):
    print(f'MORREU! \n'
          f'A palavra secreta era {palavra_secreta}!')

if __name__ == '__main__':
    jogar()
