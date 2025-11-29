'''
Exercício 2: Classe Círculo

Objetivo: Usar um setter para validar dados numéricos e ter métodos que usam a property.

Requisitos:
1. Crie uma classe Circulo com um atributo protegido _raio.
2. Crie uma @property para raio.
3. Crie um @raio.setter que valide se o valor do raio é um número positivo.
4. Crie um método calcular_area() que use a propriedade self.raio para retornar a área
do círculo (A=π⋅r2).
5. Instancie um círculo, teste a alteração do raio para um valor válido e um inválido, e
imprima a área.

'''
from math import pi

class Circulo:
    def __init__(self, raio: int):
        self._raio = raio

    @property
    def raio(self) -> int:
        return self._raio

    @raio.setter
    def raio(self, novo_raio: int):
        if novo_raio > 0 and isinstance(novo_raio, int):
            self._raio = novo_raio
        else:
            print('erro! O novo raio deve ser positivo e inteiro: ')
     
    def calcular_area(self) -> float:
        area = pi*self.raio**2
        print(area)

rodar = Circulo(2)
print(rodar.raio)
rodar.calcular_area()