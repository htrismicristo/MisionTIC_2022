# Importando librerias
import math

# Definiendo variables
articulos = []
precios = []
numcompras = int(input())

# Asignando inputs a variables
for i in range(numcompras):
    articulos.append(input())
    precios.append(int(input()))

# Computando total con descuento
if sum(precios) > 700000:
    descuento = sum(precios)*0.2
    total = sum(precios) - descuento 
   
elif sum(precios) > 300000:
    descuento = sum(precios)*0.15
    total = sum(precios) - descuento 

elif sum(precios) > 150000:
    descuento = sum(precios)*0.1
    total = sum(precios) - descuento 

else:
    descuento = 0
    total = sum(precios)

# Imprimiendo resultados
titular = "Centro Comercial Unaleño\nCompra más y Gasta Menos\nNIT:899.999.063"
dcto = f'En esta compra tu descuento fue ${math.floor(descuento)}'
agradecimientos = 'Gracias por tu compra'
total_compra = f'Total: ${math.ceil(total)}'
productos = ''
# Concatenando productos y precios en líneas nuevas cada uno
for i in range(numcompras):
    if i == numcompras-1:
        productos += str(articulos[i]) + ' $' + str(precios[i])
        break
    productos += str(articulos[i]) + ' $' + str(precios[i]) + '\n'

print(titular, productos, total_compra, dcto, agradecimientos, sep = '\n')