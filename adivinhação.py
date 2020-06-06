print('**************************************')
print('Seja bem vindo ao jogo de Adivinhação!')
print('**************************************')

numero_secreto = 42

chute = int(input('Digite o seu número: '))

acertou = chute == numero_secreto
maior   = chute > numero_secreto
menor   = chute < numero_secreto

print(f'Você chutou {chute}!')

if (acertou):
    print('Você acertou!')
else:
    if(maior):
        print('Você Errou! Seu chute foi maior que o número secreto!')
    elif(menor):
        print('Você Errou! Seu chute foi menor que o número secreto!')

print('Fim de Jogo!')