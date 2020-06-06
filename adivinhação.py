print('**************************************')
print('Seja bem vindo ao jogo de Adivinhação!')
print('**************************************')

numero_secreto = 42
total_de_tentativas = 5
rodada = 1

while (rodada <= total_de_tentativas):
    print(f'{rodada}ª tentativa de {total_de_tentativas}!')
    chute = int(input('Digite o seu número: '))

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
        print('Você acertou!')
    else:
        if(maior):
            print('Você Errou! Seu chute foi maior que o número secreto!')
        elif(menor):
            print('Você Errou! Seu chute foi menor que o número secreto!')

    rodada = rodada + 1

print('Fim de Jogo!')