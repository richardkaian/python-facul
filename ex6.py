num = int(input("Digite um numero inteiro: "))
if num > 10 or num < 1:
    print("Número inválido! Por favor, insira um número entre 1 e 10.")
else:
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")