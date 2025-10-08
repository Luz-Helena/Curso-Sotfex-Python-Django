'''
Construindo uma Mini-Escola
Imagine que você precisa criar um pequeno sistema para organizar informações de uma escola. 
A ideia é que o computador saiba quem são as pessoas, quem são os estudantes, e o que eles estão aprendendo.

Etapa 1: A Pessoa (no arquivo pessoa.py)
Toda escola tem pessoas. Um estudante é uma pessoa, um professor é uma pessoa. 
Vamos criar um "molde" básico para qualquer pessoa.

Seu trabalho aqui:
● Crie uma classe (o nosso molde) chamada Pessoa.
● Essa classe deve ter um nome e uma idade.
● Para garantir que as informações sejam acessadas e modificadas de forma organizada, 
implemente um método "getter" para o nome. Um "getter" é uma forma de obter a informação de um objeto.

'''
class Pessoa():
    def __init__(self, nome, idade):
        self.__nome = nome 
        self.idade = idade
    
    def gef_nome (self):
        return self.__nome
    
    def apresentar(self):
        print(f'Meu nome é {self.__nome} tenho {self.idade} anos')
    
pessoa1 = Pessoa('Ramon',65)

lista = [pessoa1]

for l in lista:
     l.apresentar()