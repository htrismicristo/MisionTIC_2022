# Definiendo variables
retiro = int(input())
retirado = 0

# Cantidad de billetes de 100k, 50k, 20k y 10k
billete_100 = retiro//100000
retirado += billete_100*100000
billete_50 = (retiro - retirado)//50000
retirado += billete_50*50000
billete_20 = (retiro - retirado)//20000
retirado += billete_20*20000
billete_10 = (retiro - retirado)//10000

# Imprimiendo cantidad de billetes a entregar
print(f'{billete_100} x $100000',
      f'{billete_50} x $50000',
      f'{billete_20} x $20000',
      f'{billete_10} x $10000', sep = '\n')