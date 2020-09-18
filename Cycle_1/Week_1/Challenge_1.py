nombre = input()
CU = int(input())
PVP = int(input())
UD = int(input())

print(
    'Producto: ' + nombre,
    'CU: $' + str(CU),
    'PVP: $' + str(PVP),
    'Unidades Disponibles: ' + str(UD),
    'Ganancia: $' + str((PVP-CU)*UD),
    sep = '\n'
     )
      