''''
Desafio de Programação: Validação de Triângulo
Seu objetivo: 
Escrever um algoritmo em Python que determine se:
três valores, fornecidos pelo usuário, podem formar um triângulo.

As Regras do Jogo
1- Teste se a entrada de dados é um número.
2- Se for um número teste se é positivo
3- Para que três lados (lA,lB,lC) formem um triângulo, eles devem obedecer a duas
condições importantes:

A soma: A soma de quaisquer dois lados deve ser maior que o terceiro lado.

lA<lB+lC

lB<lA+lC

lC<lA+lB

A diferença: O valor absoluto da diferença entre dois lados deve ser menor que o terceiro lado.

lA>∣lB−lC∣

lB>∣lA−lC∣

lC>∣lA−lB∣

Dica: use o método abs() para ter o valor absoluto de um número.
'''
def numero_positivo(valor):
    try:
        numero = float(valor)
        if numero > 0:
            return numero
        else:
            print("O valor deve ser um número positivo.")
            return None
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
        return None

def formar_triangulo(a, b, c):
    condicao_soma = a < b + c and b < a + c and c < a + b
    
    condicao_diferenca = a > abs(b - c) and b > abs(a - c) and c > abs(a - b)
    return condicao_soma and condicao_diferenca

lado_a = None
lado_b = None
lado_c = None

while lado_a is None:
    lado_a = numero_positivo(input("Digite o valor do lado A: "))

while lado_b is None:
    lado_b = numero_positivo(input("Digite o valor do lado B: "))

while lado_c is None:
    lado_c = numero_positivo(input("Digite o valor do lado C: "))

if formar_triangulo(lado_a, lado_b, lado_c):
    print("Os valores podem formar um triângulo!")
else:
    print("Os valores NÃO podem formar um triângulo.")
