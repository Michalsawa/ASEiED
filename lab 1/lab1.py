#5000 liczb
import numpy as np
import time

list = np.random.random_integers(0,1000,5000)

list_bab = []
list_wyb = []
list_qui = []

#babelkowe ------------------------------------



for i in range(len(list)):
    list_bab.append(list[i])
    list_wyb.append(list[i])
    list_qui.append(list[i])

    
print('babelkowe')

start = time.time()
i=0
while(True):
    if(i<len(list_bab)-1 and list_bab[i] > list_bab[i+1]):
        buf = list_bab[i]
        list_bab[i] =  list_bab[i + 1]
        list_bab[i + 1] = buf
        if(i> 0):
            i=i-1

    else:
        i = i +1
        if(i == len(list_bab)):
            break
finish = time.time()
print(finish-start)
#print (list_bab)
#sortowanie przez wybor------------------------------------------


print('\nwybor')
min = 1001
start = time.time()
for i in range(len(list_wyb)):
    for j in range(len(list_wyb)):
        if(j>=i and list_wyb[j] < min):
            min = list_wyb[j]
            buf = j
    list_wyb[buf] = list_wyb[i]
    list_wyb[i] = min
    min =1001
finish = time.time()
print(finish-start)
#print (list_wyb)

#quicksort------------------------------------

print('\nquicksort')


#print(list_qui)


def quick_sort(a, b, list):
    mid = int((b-a)/2)
    mid = mid + a
    buf = mid
    i=a
    j=a
    buf=list[mid]
    list[mid]=list[b]
    list[b]=buf
    flaga= False
    while(i<b):
        if(list[i] > buf and flaga == False):
            flaga = True
            j=i
        if(list[i]< buf and flaga):
            pom = list[j]
            list[j]=list[i]
            list[i]=pom
            j=j+1
        i=i+1
    if(flaga):
        list[b]=list[j]
        list[j]=buf
        return(j)
    else:
        return(b)
def sortowanie(a, b, list):
    if(a<b):
        j = quick_sort(a,b, list)
        sortowanie(a, j-1, list)
        sortowanie(j+1, b, list)

        
start = time.time()
        
sortowanie(0,len(list_qui)-1, list_qui)

finish = time.time()
print(finish-start)



#print(list_qui)

