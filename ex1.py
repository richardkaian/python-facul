a = int(input("Digite o primeiro numero inteiro: "))
b = int(input("Digite o segundo numero inteiro: "))

if a < b:
    menor = a
    maior = b
else:
    menor = b
    maior = a

print("Números entre", a, "e", b, ":")
for numero in range(menor, maior + 1):
    print(numero, end=" ")
print()
