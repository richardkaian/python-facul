print("Votação para o cargo de gerente:")
print("1 - João")
print("2 - Maria")
print("3 - Carlos")
print("4 - Ana")
print("5 - Voto nulo")
print("6 - Voto em branco")
joao = 0
maria = 0
carlos = 0
ana = 0
votos_nulos = 0
votos_em_branco = 0
contador = 1
colaborador = input("Digite o número correspondente ao seu voto: ")
while contador != 20:
    contador += 1
    if colaborador == "1":
        print("Voto registrado para João.")
        joao += 1
    elif colaborador == "2":
        print("Voto registrado para Maria.")
        maria += 1
    elif colaborador == "3":
        print("Voto registrado para Carlos.")
        carlos += 1
    elif colaborador == "4":
        print("Voto registrado para Ana.")
        ana += 1
    elif colaborador == "5":
        print("Voto nulo registrado.")
        votos_nulos += 1
    elif colaborador == "6":
        print("Voto em branco registrado.")
        votos_em_branco += 1
    else:
        print("Opção inválida. Voto não registrado.")
    print("Votação para o cargo de gerente:")
    print("1 - João")
    print("2 - Maria")
    print("3 - Carlos")
    print("4 - Ana")
    print("5 - Voto nulo")
    print("6 - Voto em branco")
    colaborador = input("Digite o número correspondente ao seu voto: ")
    
soma = joao + maria + carlos + ana + votos_nulos + votos_em_branco
print("Resultado da votação:")
print(f"João: {joao} votos")
print(f"Maria: {maria} votos")
print(f"Carlos: {carlos} votos")
print(f"Ana: {ana} votos")
print(f"Votos nulos: {votos_nulos} e a porcentagem de votos nulos é: {votos_nulos/soma*100:.2f}%")
print(f"Votos em branco: {votos_em_branco} e a porcentagem de votos em branco é: {votos_em_branco/soma*100:.2f}%")