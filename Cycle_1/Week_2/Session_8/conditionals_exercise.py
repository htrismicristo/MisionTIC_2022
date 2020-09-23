
# Definiendo variables
A = int(input()) 
B = int(input()) 
C = int(input()) 
D = int(input())

# Comparando variables
if B > C and D > A and (C+D) > (A+B) and D > 0 and C > 0 and (not A%2):
    print('Valores aceptados')
else:
    print('Valores no aceptados')