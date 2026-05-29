numero = int(input("Digite um número inteiro: "))
total = 1
total2 = 0
for i in range (numero, 1, -1):
    total *= i
    print(total)
    