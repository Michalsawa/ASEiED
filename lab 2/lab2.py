import numpy as np
import math

#['A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6]
i = math.inf
nodes = ['A','B','C','D','E','F','G']
#             A  B  C  D  E  F  G
graph = {'A':[i, i, 1, 2, i, i, i],
         'B':[i, i, 2, i, i, 3, i],
         'C':[1, 2, i, 1, 3, i, i],
         'D':[2, i, 1, i, i, i, 1],
         'E':[i, i, 3, i, i, 2, i],
         'F':[i, 3, i, i, 2, i, 1],
         'G':[i, i, i, 1, i, 1, i]}

poczatek  = 'A'
koniec    = 'F'



def polaczenie(znak):
    list=[]
    for i in range(len(graph)):
        if(graph[znak][i]!=math.inf):
            list.append(nodes[i])
    return list

def odleglosc(poczatek, koniec):
    for i in range(len(graph)):
        if(nodes[i] == koniec):
            return graph[poczatek][i]

def wartosc(znak):
    for i in range(len(nodes)):
        if(nodes[i]==znak):
            break
    return odleglosc(znak,nodes[i])

def zastap(znak, wartosc):
    for i in range(len(nodes)):
        if(nodes[i]==znak):
            break
    graph[znak][i] = wartosc

def sciezka(znak, start):
    for j in range(len(nodes)):
            if(graph[znak][j] == 0):
                graph[znak][j] = math.inf
                break
    for w in range(len(nodes)):
        if(nodes[w]==start):
            break
    graph[znak][w] = 0

#T=['A','B','C','D','E','F','G']
S=[]
zastap(poczatek, 0)
#max = math.inf
start = poczatek
while(True):
    max = math.inf
    S.append(start)
    if(len(S) == len(nodes)):
        break
    buf = polaczenie(start)
    list=[]
    for i in range(len(buf)):
        pom = True
        for j in range(len(S)):
            if(buf[i] == S[j]):
                pom = False
        if(pom):
            list.append(buf[i]) 
    
    for i in range(len(list)):
        if(wartosc(list[i]) > odleglosc(start, list[i]) + wartosc(start)):
            zastap(list[i],odleglosc(start, list[i]) + wartosc(start))
            sciezka(list[i],start)
    for i in range(len(nodes)):
        pom = True
        for j in range(len(S)):
            if(nodes[i] == S[j]):
                pom = False
        if(pom):
            if(max >  wartosc(nodes[i])):
                max =  wartosc(nodes[i])
                next = nodes[i]

    
    start = next
    #break

   
   # print(next)
#print(graph['D'][0])
znak = koniec
droga=[]
#print(graph)
while(znak != poczatek):
    droga.append(znak)
    print(znak)
    list = polaczenie(znak)
    for i in range(len(list)):
        if(odleglosc(znak,list[i]) == 0):
            znak = list[i]
            break

print(poczatek)
print(wartosc(koniec))
