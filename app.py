import math

print(' ')

a = int(input('Digite um número: '))
calculo = input('Digite o calculo desejado, ou sinal: ')
b = int(input('Digite o segundo número: '))

print(' ')



if calculo == '+':
  print('O resutado da soma será de ',a+b)

elif calculo == '-':
   print('O resultado da subtração será de ',a-b)    

elif calculo == '/' and b !=0 :
   print('O resultado da divisão será de ',a/b)

elif calculo == '*':
   print('O resultado da multiplicação será de ',a*b)

elif calculo == 'potencia' or calculo == 'Potência' or calculo == 'potência' or calculo == 'POTENCIA'or calculo == 'POTÊNCIA'or calculo == ' Potência'or calculo == ' potencia'or calculo == ' potência'or calculo == '^'or calculo == 'elevado por'or calculo == 'Elevado por':
   print('O primeiro número elevado pelo segundo terá o resultado de: ',math.pow(a, b))

elif calculo == 'raiz' or calculo == 'Raiz' or calculo == 'RAIZ' or calculo == 'raiz quadrada'or calculo == 'Raiz quadrada'or calculo == 'raiz Quadrada'or calculo == 'Raiz Quadrada'or calculo == 'RAIZ quadrada'or calculo == 'raiz QUADRADA'or calculo == 'RAIZ QUADRADA'or calculo == 'Raiz QUADRADA':
   print('A raiz quadrada do primeiro número é = ',math.sqrt(a),'. e a do segundo número será = ', math.sqrt(b) )

else:
   print('Não possuirá valor numerico')

print(' ')
