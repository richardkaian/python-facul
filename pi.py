print("Cargos: ")
print("1 - Enfernmeiro")
print("2 - Nutricionista")
print("3 - Médico")
print("0 - Sair")

cargo = int(input("Digite o cargo: "))
cont = 0
sal_total = 0
sal_medico = 0
med = 0
while cargo !=0:
    salario = float(input("Digite o salário: "))
    if cargo == 2:
        cont = cont + 1
        sal_total = sal_total + salario
    if cargo == 3 and salario >4500:
        med = med + 1
    print("Cargos: ")
    print("1 - Enfernmeiro")
    print("2 - Nutricionista")
    print("3 - Médico")
    print("0 - Sair")
    cargo = int(input("Digite o cargo: "))
media = sal_total / cont
print(media)
print(f"A quantidade de médicos com salario superior a 4.500 é {med}")
    
