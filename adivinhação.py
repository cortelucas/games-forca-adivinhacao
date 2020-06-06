import random

print('**************************************')
print('Seja bem vindo ao jogo de Adivinhação!')
print('**************************************')

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 5

for rodada in range(1, total_de_tentativas+1):
    print(f'{rodada}ª tentativa de {total_de_tentativas}!')
    chute = int(input('Digite um número entre 1 e 100: '))

    if (chute < 1 or chute > 100):
        print('Você deve digitar um número entre 1 e 100!')
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
        print('Você acertou!')
        break
    else:
        if(maior):
            print('Você Errou! Seu chute foi maior que o número secreto!')
        elif(menor):
            print('Você Errou! Seu chute foi menor que o número secreto!')

    rodada = rodada + 1

print('Fim de Jogo!')
