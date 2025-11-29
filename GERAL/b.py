# EXERCICIO 1

numero =int(input("Digite um numero inteiro: "))
for i in range(1,11):
        print(f"{numero} x {i}: = {numero*i}")

# EXERCICIO 2
palavra = input("Digite uma palavra: ")
contador_vogais = 0
vogais = "aeiou"
for letra in palavra.lower():
    if letra in vogais:
        contador_vogais +=1
print(f"A palavra tem {contador_vogais} vogais.")

# EXERCICIO 3
maior = float(-10000000000)
for i in range(5):
    num = int(input(f"Digite o {i+1}º numero: "))
    if num > maior:
        maior = num    
print(f"O maior numero é: {maior}")

# EXERCICIO 4
altura= int(input("Digite a altura do triângulo: "))
for i in range(altura):
    linha = ""
    for j in range(i+1):
        linha+="*"
    print(linha)

# EXERCICIO 4
altura= int(input("Digite a altura do triângulo: "))
for i in range(altura):
      print("*"*(i+1))
      
# EXERCICIO token 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
# EXERCICIO 
# EXERCICIO 
# EXERCICIO 
