preço_original = float(input("Digite o preço do produto: "))

if preço_original > 100:
     desconto = 0.10
     valor_desconto = preço_original * desconto
     preço_final = preço_original - valor_desconto
     print(f"Voce posssui desconto!! Valor:{valor_desconto: .2f} reais")
     print(f"Valor final:{preço_final: .2f} reais") 

else:
     print(f"Valor sem desconto:{preço_original: }.")  