'''
Nível 4: Desafio Final

Este é o exercício mais completo, combinando entrada de dados do usuário, loops, validação
e manipulação de listas.

Exercício 4: Coletor de Dados Robusto

Crie um programa que colete números de usuário e os armazene em uma lista. O programa
deve continuar pedindo números até que o usuário digite -1 para parar. Ele deve validar a
entrada para garantir que o que foi digitado é realmente um número antes de prosseguir.
Apenas os números entre 0 e 100 devem ser considerados válidos e adicionados à lista. Ao
final, imprima a soma dos números válidos e a lista dos números coletados.

● Entrada: Vários valores digitados pelo usuário, um de cada vez.
● Saída: A soma dos números válidos e a lista dos números coletados.

Exemplo:
Entradas: 10, 50, abc, -5, 101, 20, -1

Resultado Esperado:
Soma dos números válidos: 80
Números coletados: [10, 50, 20]

'''

numeros = 10, 50, abc, -5, 101, 20, -1
numero_soma = []
coletas = 0

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
