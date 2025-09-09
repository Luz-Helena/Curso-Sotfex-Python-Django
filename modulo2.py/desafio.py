
usuario = input("Digite o nome do usuário (ou 'parar' para sair): ")
status = input("Selecione o status: \n 1.sucesso \n 2.falha \n Opção: ")
duracao_minutos = input("Digite a duração da sessão em minutos: ")

while usuario != 'parar':
    try:
        duracao_minutos = int(duracao_minutos)
    except:
        print("Duração inválida. Por favor, insira um número inteiro.")
        continue
    if(status == '1'):
        registros_acessos = [(usuario, status, duracao_minutos)]

print(f"Registro de acesso bem-sucedido: {registros_acessos}")
