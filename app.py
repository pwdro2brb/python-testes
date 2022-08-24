print(' ')

print('Exercicio 5')
print('\n Boletim escolar\n')

n = input('Digite o nome do aluno: ')

not1 = int(input('Digite o valor da nota do 1º bimestre: '))
not2 = int(input('Digite o valor da nota do 2º bimestre: '))
not3 = int(input('Digite o valor da nota do 3º bimestre: '))
not4 = int(input('Digite o valor da nota do 4º bimestre: '))

med =  not1+not2+not3+not4

if med >= 60 and med < 100:
  print('O aluno ',n,' está aprovado! Com uma nota final de ',med)
elif med < 60 and med >=0:
  print('O aluno ',n,' está reprovado! Com uma nota final de ',med)
else:
  print('Valor fora da curva --> ', med)

print(' ')