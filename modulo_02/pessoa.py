class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."

    def __str__(self):
        return self.apresentar()

joao = Pessoa("João", 25)
maria = Pessoa("Maria", 30)
print(joao)
print(maria)



class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def apresentar_produto(self):
        return f"Produto {self.nome}, preço {self.preco}."

    def __str__(self):
        return self.apresentar_produto()

caderno = Produto("Caderno", 15.50)
caneta = Produto("Caneta", 3.00)
print(caderno)
print(caneta)

class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Depósito de {valor} realizado. Novo saldo: {self.saldo}."
        else:
            return "Valor de depósito deve ser positivo."

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            return f"Saque realizado com sucesso"
        else:
            return "Saldo insuficiente."

    def __str__(self):
        return f"Conta de {self.titular}, Saldo: {self.saldo}."

conta_joao = ContaBancaria("João", 100)
print(conta_joao)
print(conta_joao.depositar(50))
print(conta_joao.sacar(80))
print(conta_joao)

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

    def __str__(self):
        return f"Retângulo de base {self.base} e altura {self.altura}."

retangulo1 = Retangulo(2, 4)
print(retangulo1)
print(f"Área: {retangulo1.calcular_area()}")
print(f"Perímetro: {retangulo1.calcular_perimetro()}")

class Carro:
    def __init__(self, modelo, nivel_combustivel=0):
        self.modelo = modelo
        self.nivel_combustivel = nivel_combustivel

    def abastecer(self, litros):
        return self.nivel_combustivel + litros

    def dirigir(self, distancia):
        consumo_por_km = 1 / 10  # 1 litro a cada 10 km
        combustivel_necessario = distancia * consumo_por_km
        if self.nivel_combustivel >= combustivel_necessario:
            self.nivel_combustivel -= combustivel_necessario
            print(f"O carro {self.modelo} percorreu {distancia} km.")
        else:
            print(f"Combustível insuficiente para percorrer {distancia} km.")

    def __str__(self):
        return f"O carro é {self.modelo} e tem {self.nivel_combustivel} litros de combustível."

meu_carro = Carro("Fusca", 5)
meu_carro.abastecer(30)
meu_carro.dirigir(50)
meu_carro.dirigir(500)

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        self.percentual_bonus = 1.10

    def aplicar_bonus(self):
        aumento = self.salario * self.percentual_bonus
        self.salario += aumento
        return f"Salário de {self.nome} aumentado para {self.salario}."

    def __str__(self):
        return f"Funcionário: {self.nome}, Salário: {self.salario}."

funcionario1 = Funcionario("Ana", 2000)
print(funcionario1)
print(funcionario1.aplicar_bonus())
print(funcionario1)
funcionario2 = Funcionario("Joao", 5000)
print(funcionario2)
print(funcionario2.aplicar_bonus())
print(funcionario2)

class Motor:
    def __init__(self, potencial):
        self.potencial = potencial

class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.motor = Motor(100)

    def exibir_potencia(self):
        return f"O carro {self.modelo} tem um motor de potencia {self.motor.potencial}."

    def __str__(self):
        return self.exibir_potencia()

meu_carro = Carro("Chevete")
print(meu_carro)

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Biblioteca:
    def __init__(self):
        self.acervo = []

    def adicionar_livro(self, livro):
        self.acervo.append(livro)

    def listar_livros(self):
        for livro in self.acervo:
            print(f"Livro {livro.titulo}, autor {livro.autor}")

minha_biblioteca = Biblioteca()
livro1 = Livro("Dom Casmurro", "Machado de Assis")
livro2 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry")
livro3 = Livro("Capitães da Areia", "Jorge Amado")
minha_biblioteca.adicionar_livro(livro1)
minha_biblioteca.adicionar_livro(livro2)
minha_biblioteca.adicionar_livro(livro3)
minha_biblioteca.listar_livros()

class Filme:
    def __init__(self, titulo, diretor, ano):
        self.titulo = titulo
        self.diretor = diretor
        self.ano = ano

    def __str__(self):
        return f"Filme: {self.titulo}, Diretor: {self.diretor}, Ano: {self.ano}"

meu_filme = Filme("A espera de um milagre", "Frank Darabont", 1999)
print(meu_filme)
