print(' ')

arqu_pa = open("C:/Users/User/Desktop/python testes/paises.txt", "r", encoding="utf8")#abre o outro arquivo nesse outro local
print(arqu_pa.readline()[0])#inprime a primeira linha e a primeira letra do outro documento

print(' ')
print(arqu_pa.readline())#Agora ele irá inprimir a segunda linha do outro documento
print(arqu_pa.readline(3))#terceira linha e os trés primeiros valores dela 
print(' ')

print(arqu_pa.readable())#inprime se o outro arquivo é "legivel"
print(' ')

for files in arqu_pa.readlines():#inprime todas as linhas restantes com espaço (quebra de linha)
   print(files)
arqu_pa.close
print(' ')



