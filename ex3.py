i = 1

while i <= 15:
    nota = float(input("Digite a nota de  (0 a 5): "))
    if nota >= 0 and nota <= 5:
        print("Nota", i, "registrada:", nota)
        i = i + 1
    else:
        print("Nota inválida! Insira um valor entre 0 e 5.")
