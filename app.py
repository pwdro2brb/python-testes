
d = int(input(' d = '))
c = int(input(' c = '))
b = input(' b = ')
a = input(' a = ')


print(' ')

if a < b:
   print(str(a) +' é maior que '+ str(b))
elif a == b:
   print(str(a) + ' = '+str(b))
else:
   print('a não é maior que b')

print(' ')
if a := b:
   print(' a é igual a b ')

print(' ')

if type(c) == str:
   print('O valor de c digitado é um string')
else:
   print('O valor de c digitado não é um string')

print(' ')

if d%5==0:
   print('O valor de d é divisivel por 5')
else:
   print('O valor de d não é divisivel por 5')


print(' ')