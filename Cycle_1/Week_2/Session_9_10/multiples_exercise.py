# definiendo variables
n = int(input("digite n:"))
m = int(input("digite m:"))
multiplos = []

# Calculando múltiplos
if n < m:
    multiplos.append(0)
else:
    for i in range(n+1):
        if not i%m:
            multiplos.append(i)

# Generando formato de resultados
resultados = 'Los múltiplos son:'
for i in multiplos:
    resultados += '\n' + str(i)

# Imprimiendo los resultados
print(resultados)