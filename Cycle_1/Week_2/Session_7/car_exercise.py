# importando librerías
import math

# Definiendo variables
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
r1 = int(input())
r2 = int(input())


# Computando áreas
area_circulo1 = math.pi*r1**2
area_circulo2 = math.pi*r2**2
area_rectangulo1 = a1*b1
area_rectangulo2 = a2*b2

# Computando la suma de áreas
suma_areas = area_circulo1 + area_circulo2 + area_rectangulo1 + area_rectangulo2

# impriendo resultados
print('suma total = {}'.format(suma_areas))