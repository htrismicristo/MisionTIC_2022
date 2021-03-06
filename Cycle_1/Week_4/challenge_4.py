# Importa librerias
import math
import json
import requests

# Define variables importantes 
articulos = []
precios = []
cantidades = []
tirillas = []


# Recupera el archivo json y extrae la lista de compras
response = requests.get(input())
clientes = json.loads(response.text)

# Extrae las compras realizadas por cada cliente
for i in range(len(clientes)):
    for j in range(len(clientes[i]['productos'])):
        articulos.append(clientes[i]['productos'][j]['nombre'])
        cantidades.append(clientes[i]['productos'][j]['cantidad'])
        precios.append(clientes[i]['productos'][j]['precio unitario'])

    # computa el valor total de la venta
    venta = []
    for units, p in zip(cantidades, precios):
        venta.append(units*p)

    # Computando total con descuento
    if sum(venta) > 700000:
      descuento = sum(venta)*0.2
      total = sum(venta) - descuento 
      
    elif sum(venta) > 300000:
      descuento = sum(venta)*0.15
      total = sum(venta) - descuento 

    elif sum(venta) > 150000:
      descuento = sum(venta)*0.1
      total = sum(venta) - descuento 

    else:
      descuento = 0
      total = sum(venta)

    # Generando tirillas
    titular = "Centro Comercial Unaleño\nCompra más y Gasta Menos\nNIT:899.999.063"
    cc_cliente = f"Cliente: {clientes[i]['cliente']}"
    labels = "Art Cant Precio"
    dcto = f'En esta compra tu descuento fue ${math.floor(descuento)}'
    agradecimientos = 'Gracias por tu compra'
    total_compra = f'Total: ${math.ceil(total)}'
    productos = ''
    separator = "---"

    # Concatenando productos, cantidades y precios en líneas nuevas cada uno
    for i in range(len(articulos)):
        if i == (len(articulos)-1):
            productos += str(articulos[i]) + ' ' + 'x' + str(cantidades[i]) + ' $' + str(precios[i]*cantidades[i])
            break
        productos += str(articulos[i]) + ' ' + 'x' + str(cantidades[i]) + ' $' + str(precios[i]*cantidades[i]) + '\n'
    
    # Vacía los atributos de la compra en el carro
    articulos = []
    precios = []
    cantidades = []
    
    # Acumula las tirillas hasta que el cliente sale
    tirillas.append("\n".join([titular, cc_cliente, labels, productos, total_compra, dcto, agradecimientos, separator]))

for tirilla in tirillas:
  print(tirilla)