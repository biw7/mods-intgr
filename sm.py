import compil
import sm2

arq = input ('Nome do arquivo:')
fA = open(arq)
A = fA.read()
link = A.split()
titulo = A.split()
tam = len(link)

for i in range (tam):
    titulo[i] = sm2.titulo(link[i])
    link[i] = compil.sh(2,link[i])

for i in range (tam):
    print (titulo[i], '...: ',link[i])


