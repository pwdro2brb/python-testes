print(' ')

print('Exercicio 4')
print('\n MDC, minimo e máximo divisor comun\n')

x = int(input('Digite um valor de um número: '))
y = int(input('Digite um valor de outro número: '))
i = 1

if x == 0 or y == 0:
  print('O menor divisor comun entre ambos é: 0')
elif x==y:
  print('o maior divisor comun entre ambos é: ',x)
elif y > x:
  i = y % x
  print('O maior divisor comun entre ambos é: ',i)
elif x > y:
  i = x % y
  print('O maior divisor comun entre ambos é: ',i)


print(' ')