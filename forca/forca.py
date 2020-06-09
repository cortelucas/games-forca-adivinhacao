def jogar():
    print('*************************************')
    print('*****Bem vindo ao jogo de Forca!*****')
    print('*************************************')

    palavra_secreta = 'banana'.upper()
    letras_acertadas = ['_', '_', '_', '_', '_', '_']

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not enforcou and not acertou):
        chute = input('Qual letra? ')
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            i = 0
            for letra in palavra_secreta:
                if (chute == letra.upper()):
                    letras_acertadas[i] = letra
                i += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print('Parabéns! Você ganhou!')
    else:
        print('Que pena! Perdeu!')
    print('Fim do Jogo!')


if __name__ == '__main__':
    jogar()
