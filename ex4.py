soma= 0
cont = 0
temp = 0
while temp != -273:
    temp = float(input("Digite a temperatura (ou -273 para sair): "))
    if temp != -273:
        soma = soma + temp
        cont = cont + 1

if cont > 0:
    media = soma / cont
    print(f"A média das temperaturas é: {media}")
else:
    print("Nenhuma temperatura válida foi inserida.")