
from ast import Return


a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))




print(' ')

if b*b-4*c*a > 0 :
   print('Duas raízes reais')
elif b*b-4*c*a == 0:
   print('Uma raiz real')
elif b*b-4*c*a < 0:
   print('Nenhuma raiz real')
else:
   print('Digite números para mostrar se há raizes reais')

print(' ')
