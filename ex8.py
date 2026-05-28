jovem = 0
adulto = 0
velho = 0
idoso = 0
idade = int(input("Digite a idade: "))
while idade > 0:
    if idade > 0 and idade <= 25:
        jovem = jovem + 1
    elif idade > 25 and idade <= 50:
        adulto = adulto + 1
    elif idade > 50 and idade <= 75:
        velho = velho + 1
    else:
        idoso = idoso + 1
    idade = int(input("Digite a idade: "))
print("Jovens:", jovem)
print("Adultos:", adulto)
print("Velhos:", velho)
print("Idosos:", idoso)