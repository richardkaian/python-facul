n = int(input("Verificar número primo: "))

mult = 0

for count in range(2, n):
    if n % count == 0:
        print(f"Múltiplo de {count}")
        mult += 1

if mult == 0 and n > 1:
    print("É primo")
else:
    print(f"Tem {mult} múltiplos acima de 2 e abaixo de {n}")