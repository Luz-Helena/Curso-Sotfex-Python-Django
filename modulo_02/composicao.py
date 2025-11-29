'''
1. Montando um Carro (Fácil)
● Classes: Motor e Carro.

● Classe Motor:
○ Método: __init__ (sem atributos).
○ Método: ligar() que imprime "O motor ligou.".

● Classe Carro:
○ Atributo (Composição): motor, que deve ser uma instância de Motor.
○ Método: __init__ que inicializa o atributo motor.
○ Método: ligar_carro() que chama o método ligar() do seu objeto motor.
'''

class Motor:
    def ligar_motor(self):
        print('O motor ligou.')

    def desligar_motor(self):
        print('MOto desligou!')

class Carro:
    def __init__(self):
        self.motor = Motor()

    def ligar(self):
        print('O carro esta ligando...')
        self.motor.ligar_motor()

rodar = Carro()
rodar.ligar()

'''
2. Criando uma Cafeteira (Fácil)
● Classes: GraoDeCafe, Agua e Cafeteira.

● Classe GraoDeCafe:
○ Método: __init__ (sem atributos).
○ Método: moer() que imprime "Os grãos de café foram moídos.".

● Classe Agua:
○ Método: __init__ (sem atributos).
○ Método: aquecer() que imprime "A água está aquecida.".

● Classe Cafeteira:
○ Atributos (Composição): grao e agua, que devem ser instâncias das classes
GraoDeCafe e Agua.
○ Método: __init__ que inicializa os atributos grao e agua.
Método: preparar_cafe() que chama os métodos moer() do seu grao e aquecer() da
sua agua.
'''
class GraoDeCafe:
    def moer_graos(self):
        print('Os grãos de café foram moídos.')

class Agua:
    def aquecer_agua(self):
        print('A água está aquecida.')

class Cafeteira:
    def __init__(self):
        self.grao = GraoDeCafe()
        self.agua = Agua()
    
    def preparar_cafe(self):
        self.grao.moer_graos()
        self.agua.aquecer_agua()
        print('Café pronto')

rodar = Cafeteira()
rodar.preparar_cafe()

