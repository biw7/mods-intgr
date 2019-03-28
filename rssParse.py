#Essa é a função main

import feedparser
from datetime import datetime
import compil
import listaURLs
import tradutor

data=datetime.now()

lista = listaURLs.listaURLs
tam = len(lista)
for i in range (tam):
    print (i,":",lista[i],"\n")

n = input ("Opção:")
opTrad = input ('Traduzir (s/n)')
link = listaURLs.listaURLs[int(n)]
tFunk = feedparser.parse(link)
c = []
op = int (input("0-url_Original\n1-ClicksFly\n2-Rebrandly\n"))
print(data)
for i in range (10):
    item = tFunk.entries[i]
    item['link'] = compil.sh(op,item['link'])
    if opTrad == 's':
        item['title'] = tradutor.trad(item['title'])
    print (item['title' ],'\n',item['link'],'\n\n')
    c.append(item['title' ])
    c.append (' -->> ')
    c.append(item['link'])
    c.append('\n')

arq = open('Arq','w')
arq.writelines (c)
arq.close()




    

