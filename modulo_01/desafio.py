"""
Comercio Padaria
1 - O programa tem que rodar em loop até ser parado
x 2 - Cliente pedir um tipo de pão (frances, doce, forma, astraliano) 
x 3 - Cada pão tem uma quantidade. 
x 4 - Forma de pagamento (dinheiro, cartão)
5 - Valor do pão
6 - Forma de entrega
7 - Dados do cliente (se for entregar)
8 - Valor do frete por bairro
x9 - Qual o nome da atentende
10 - Código da entrega


"""
nome_frances = 'Frances'
nome_doce = 'Doce'
nome_forma = 'Forma'

valor_france = 0.50
valor_doce = 5.00
valor_forma = 5.99
valor_compras = 0.00

qt_france = 15
qt_doce = 20
qt_forma = 10


nome_atendente = 'Maria'

bairro_barroco = 'barroco'
bairro_sao_jose = 'são José'

frete_barroco = 5.00
frete_sao_jose = 15.00

cod_venda = 9568

while True:
    print(f'-- Bem vindo a padaria, Desespero, sou a {nome_atendente}')
    escolha = input('Temos pães: frances, doce, forma, astraliano - Qual pão você deseja: ')
    if escolha == nome_frances:
        quantidade = int(input('Qual a quantidade? '))
        if quantidade <= qt_france:
            qt_france -= quantidade
            pedido_de_paes = quantidade
            valor_compras = quantidade * valor_france
            print(f'Seu pedido ficou em R$ {qt_france * valor_france}')
        else:
            print(f'Infelizmente só tenho {qt_forma}, pães no momento')
            break

    forma_retirada = input('O pedido será retirada? ').lower()
    if forma_retirada == 'sim':
        bairro_entrega = input(f'Qual o bairro? (1:{bairro_barroco}, 2:{bairro_sao_jose})')
        if bairro_entrega == '1':
            valor_frete = frete_barroco
        elif bairro_entrega == '2':
            valor_frete = frete_sao_jose
            print(f'Valor do frete R$ {valor_frete}')
        else:
            print('Fora da área de entrega ')
            break
    elif forma_retirada == '1':
        valor_frete = 2.00
    else:
        break

    dados_cliente = input('Digite seu nome: ')
    forma_pagamento = input('Escolha a forma de pagamento {1-dinheiro, 2-cartão}')

    if forma_pagamento =='1':
        forma_pagamento = 'Dinheiro'
    else:
        forma_pagamento = "Cartão"

    cod_atual = cod_venda + 1
    print(f'Valor total da sua compra foi de R$ {valor_compras + valor_frete} com código')
    break



"""
pao = 'frances, doce, forma, astraliano'
for paes in pao:
"""