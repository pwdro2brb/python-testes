from tokenize import ContStr
from traceback import print_list


print(' ')

print('Exercicio 7')
print('\n Progressão aritmética \n')

a1 = int(input(' Digite o valor do primeiro termo '))
n =  int(input(' Digite o número de termos '))
r =  int(input(' Digite a razão, ou seja, a quantidade que aumenta no intervalo em cada número '))

i=0


while i < n:
  print(a1)
  a1+=r
  i+=1

print(' ')

print(' ')

print('Exercicio 8')
print('\n Progressão geométrica \n')

aa1 = int(input('Digite o valor do primeiro termo '))
q = int(input('Digite o valor da razão, ou seja a quantidade de aumento no intervalo '))
n2 = int(input('Digite a quantidade de termos '))

ii=0
ann=0
print(aa1)

while ii < n2:
 ii+=1
 ann = aa1*q**ii
 print(ann)
 



print(' ')