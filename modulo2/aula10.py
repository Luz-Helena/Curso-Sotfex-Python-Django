'''
1. Nível Fácil: Registro de Pessoas

Crie uma classe base Pessoa com um construtor que recebe nome e idade. Adicione um
método apresentar() que imprime uma frase com o nome e a idade da pessoa.

Em seguida, crie uma classe Estudante que herda de Pessoa. O construtor de Estudante deve
chamar o construtor da classe pai e adicionar um atributo para o curso. A classe Estudante
deve sobrescrever o método apresentar() para incluir o curso na frase.

Por fim, crie uma lista com um objeto Pessoa e um objeto Estudante. Itere sobre a lista e
chame o método apresentar() para cada item, demonstrando o polimorfismo.
'''

class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade

    def apresentar(self):
        print(f'Meu nome é {self.nome} tenho {self.idade} anos')
    
class Estudante(Pessoa):
    def __init__(self, nome, idade,curso):
        super().__init__(nome,idade)
        self.curso = curso

def apresentar(self):
        print(f'Meu nome é {self.nome} tenho {self.idade} anos e curso {self.curso}')

pessoa1 = Pessoa('Ramon',65)

pessoa = Estudante('Guilherme',32,'Sofredor')

lista = [pessoa1, pessoa]

for l in lista:
     l.apresentar()

'''
2. Nível Médio: Sistema de Mídia

Crie uma classe base Midia com um construtor que recebe titulo e duracao_seg. Adicione um
método exibir() que imprime o título e a duração.

Crie duas classes filhas, Musica e Video, que herdam de Midia:
● Musica deve ter um atributo adicional artista e sobrescrever o método exibir() para
incluir o nome do artista.

● Video deve ter um atributo adicional resolucao e sobrescrever o método exibir() para
incluir a resolução.

No script principal, crie um dicionário para organizar sua coleção de mídias, usando as
chaves 'musicas' e 'videos'. Crie objetos de Musica e Video e os adicione a suas respectivas
listas dentro do dicionário. Por fim, itere sobre as listas e chame o método exibir() para cada
item, demonstrando o polimorfismo de forma organizada.

'''

class Midia:
    def __init__(self, titulo, duracao_seg):
        self.titulo = titulo
        self.duracao_seg = duracao_seg

    def exibir(self):
        print(f"Título: {self.titulo} Duração: {self.duracao_seg} segundos")
    

class Musica(Midia):
    def __init__(self, titulo, duracao_seg, artista):
        super().__init__(titulo, duracao_seg)
        self.artista = artista

    def exibir(self):
        super().exibir()  
        print(f"Artista: {self.artista}")
      

class Video(Midia):
    def __init__(self, titulo, duracao_seg, resolucao):
        super().__init__(titulo, duracao_seg)
        self.resolucao = resolucao

    def exibir(self):
        super().exibir()  
        print(f"Resolução: {self.resolucao}")
  

colecao_midia = {
    'musicas': [],
    'videos': []
}

musica1 = Musica("Bohemian Rhapsody", 354, "Queen")
musica2 = Musica("Shape of You", 263, "Ed Sheeran")
video1 = Video("The Matrix", 136, "1920x1080")
video2 = Video("Inception", 148, "3840x2160")


colecao_midia['musicas'].append(musica1)
colecao_midia['musicas'].append(musica2)
colecao_midia['videos'].append(video1)
colecao_midia['videos'].append(video2)

print("Exibindo músicas:\n")
for musica in colecao_midia['musicas']:
    musica.exibir()


print("Exibindo vídeos:\n")
for video in colecao_midia['videos']:
    video.exibir()

'''
3. Nível Médio/Avançado: Hierarquia de Formas Geométricas
Crie uma classe base FormaGeometrica com um construtor para cor e um método
calcular_area() que não faz nada.

Crie uma classe Retangulo que herda de FormaGeometrica e tem atributos para largura e
altura. A classe deve sobrescrever o método calcular_area().
Crie uma classe Quadrado que herda de Retangulo. O construtor deve receber apenas o lado
e passar esse mesmo valor para largura e altura da classe pai. O encapsulamento deve ser
aplicado aos atributos de dimensão.

No script principal, crie uma tupla com um objeto de Retangulo e um objeto de Quadrado.

Crie uma função chamada calcular_soma_areas() que recebe essa tupla, itera sobre ela e
soma a área de todas as formas. A função deve chamar o método calcular_area() de forma
polimórfica para cada objeto, exibindo a soma total no final.

'''

