retiro = input()
billete_100 = []
billete_50 = []
billete_20 = []
billete_10 = []

# Cantidad de billetes de 100k
try:
  billete_100.append(int(retiro[:-5]))
# Cuando no se deben entregar billetes de 100k
except:
  billete_100 = [0]

# Cantidad de billetes de 10k, 20k y 50k

# Si el retiro es número par
if not int(retiro[-5]) % 2:
  # Si es menor a 5
  if int(retiro[-5]) < 5:  
    billete_20.append(int(retiro[-5]) // 2)
  # Si es mayor o igual a 5
  else:  
    billete_50.append(int(retiro[-5]) // 5)
    billete_20.append((int(retiro[-5])-5) // 2)
    billete_10.append((int(retiro[-5])-5) % 2)

# Si el retiro es número impar
elif int(retiro[-5]) % 2: 
  # Si es menor a 5
  if int(retiro[-5]) < 5:  
    billete_20.append(int(retiro[-5]) // 2)
    billete_10.append(int(retiro[-5]) % 2)
  # Si es mayor o igual a 5
  else:  
    billete_50.append(int(retiro[-5]) // 5)
    billete_20.append((int(retiro[-5])-5) // 2)

# Imprimiendo cantidad de billetes a entregar
print(f'{sum(billete_100)} x $100000',
      f'{sum(billete_50)} x $50000',
      f'{sum(billete_20)} x $20000',
      f'{sum(billete_10)} x $10000', sep = '\n')