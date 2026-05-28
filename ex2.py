colonia_a = 4
colonia_b = 10
dias = 0

while colonia_a < colonia_b:
    colonia_a = colonia_a * 1.03
    colonia_b = colonia_b * 1.015
    dias = dias + 1

print("A Colônia A ultrapassou (ou igualou) a Colônia B após", dias, "dia(s).")
print("Colônia A:", round(colonia_a, 4), "| Colônia B:", round(colonia_b, 4))
