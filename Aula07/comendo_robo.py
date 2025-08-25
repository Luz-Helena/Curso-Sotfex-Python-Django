comando = 0

print(f'-- Seja, Bem vindo!')
while True:
    posicao = int(input(f'Escolha um comando: 1:Avançado, 2:Recuar, 3:Status, 4:Desligar '))
    if posicao == 1:
        comando += 1
    elif posicao == 2:
        comando -= 1
    elif posicao == 3:
        print(comando) 
    elif posicao == 4:
        print('Desligar')
        break

    else:
        print('Comando invalido')