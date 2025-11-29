pedido = 'x-tudo'
hamburguer = 5.99
cupom_desconto = 0.5

while True:
    food = int(input(f'Escolha o seu lanche: 1:{pedido}, 2:Outros '))
    if food == 1:
       cupom = input('Ok, possui cupom de desconto? 1:Sim, 2:Não')
       if cupom == '1':
            print(f'Valor final com desconto: {hamburguer - (hamburguer * cupom_desconto)}')
            break
       elif cupom == '2':
            print(f'Valor final do pedido {hamburguer}')
            break
    elif food == 2:
        print(f'No momento só temos {pedido}')
        continue
    else:
        print('Faça seu pedido')
    print('Pedido finalizado')
    break