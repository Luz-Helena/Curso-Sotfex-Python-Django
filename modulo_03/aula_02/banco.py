import sqlite3

conectar = sqlite3.connect('meu_banco.db')

print("Banco de dados 'meu_banco.db" foi criado com sucesso")
      
conectar.close()