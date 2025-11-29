'''
21. Agenda de Contatos: Crie um sistema simples de agenda que use um dicionário. Use
um loop while para mostrar um menu com opções de "adicionar contato", "buscar
contato" e "sair"
'''
agenda_contatos ={}

while True:
    print('Menu:')
    print('Adicionar contato')
    print('Buscar contato')
    print('Sair')

    opcao = input('Escolha uma opção')

    if opcao == "Adicionar contato":
        nome = input('Digite o nome do contato')
        telefone = input('Digite o telefone para contato:')
        agenda_contatos[nome] = telefone
        print(f'Contato {nome} adicionado com sucesso!')