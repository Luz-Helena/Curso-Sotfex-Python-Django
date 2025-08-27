# 1. Definindo o número secreto
numero_secreto = 39
tentativas = 5

print('Bem-vindo ao Jogo de Adivinhação!')
print('Tente adivinhar o número entre 1 e 100. Você tem 5 tentativas.')

# 2. Loop de tentativas
for tentativa in range(1, tentativas + 1):
    palpite = int(input(f"Tentativa {tentativa}: Digite seu palpite: "))

    if palpite == numero_secreto:
        print('Parabéns! Você acertou o número!')
        break
    elif palpite < numero_secreto:
        print('Muito baixo!')
    else:
        print('Muito alto!')

# 3. Se não acertar após todas as tentativas
else:
    print(f'Game Over!')