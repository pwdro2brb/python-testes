print(' ')

print('Exercicio 3')
print('\n login e cadastro \n')

x = input('Digite aqui o seu nome: ')
y = input('Digite aqui a sua senha: ')


print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

print('Cadastro feito com sucesso!!!!!')
print('Agora o login.\n\n')

log = input('Digite o nome usado no seu cadastro: ')
sen = input('Digite o nome usado no sua senha: ')

if log == x and sen == y:
  print('Login feito com sucesso. ') 
elif log != x:
  print('Nome do usuário incorrreto. ')
elif sen != y:
  print('Senha do usuário incorreto. ')  
else: 
  print('Usuário e senha incorreto. ')

print(' ')