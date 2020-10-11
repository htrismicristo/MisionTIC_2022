# Definiendo variables
A = int(input())
B = int(input())
day_B_surpasses_A = 1

# Definiendo ciclo While
while A > B:
    A += A*0.02
    B += B*0.03
    day_B_surpasses_A += 1

# Imprimiendo resultados
print(day_B_surpasses_A)
