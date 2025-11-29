primeiro = int(input("Digite o primeiro número: "))
segundo = int(input("Digite o segundo número: "))

if primeiro > segundo:
    print(f"O primeiro é maior:{primeiro: .1f}")
elif segundo > primeiro:
    print(f"O segundo é maior:{segundo: .1f}")
else:
    primeiro = segundo      
    print("Os números são iguais")