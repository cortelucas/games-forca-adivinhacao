print('**************************************')
print('Seja bem vindo ao jogo de Adivinhação!')
print('**************************************')

numero_secreto = 42

chute = int(input('Digite o seu número: '))

print(f'Você chutou {chute}!')

if (numero_secreto == chute):
    print('Você acertou!')
else:
    print('Você errou!')