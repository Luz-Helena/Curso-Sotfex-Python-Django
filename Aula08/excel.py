import pandas as pd

# Criar os dados da tabela (vazia para preenchimento)
data = {
    "Escritor(a)": [],
    "Nome da Obra": [],
    "Quantidade em Estoque": [],
    "Preço Unitário (R$)": [],
    "Quantidade Vendida": [],
    "Forma(s) de Pagamento": [],
    "Total Arrecadado (R$)": [],
    "Total de Livros Vendidos": []
}

# Criar o DataFrame
df = pd.DataFrame(data)

# Salvar como arquivo Excel
df.to_excel("controle_venda_livros.xlsx", index=False)

print("Arquivo Excel 'controle_venda_livros.xlsx' criado com sucesso!")
