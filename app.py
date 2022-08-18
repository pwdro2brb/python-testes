print(' ')

arqu_pa = open("C:/Users/User/Desktop/python testes/paises.txt", "r", encoding="utf8")#abre o outro arquivo nesse outro local, fará a sua leitura, e considera a codificação do outro arquivo.

print(arqu_pa.readline()[0])#inprime a primeira linha e a primeira letra do outro documento

print(' ')

print(arqu_pa.readline())#Agora ele irá inprimir a segunda linha do outro documento
arqu_pa.close

print('___________________________________')

a= open("C:/Users/User/Desktop/python testes/testoterom.txt", "w", encoding="utf8")

a.write('I got a gun, agaragan ')

a.write('\n uno')
a.close

print(' ')

b = open("C:/Users/User/Desktop/python testes/testo.py", "w")
b.write('i=1 \nwhile i<=10: \n  print(i,\'numeros\')   \n  i+=1')

print(' ')




