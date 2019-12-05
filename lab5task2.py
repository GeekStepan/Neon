from random import randint as random

def lab2(n):
    listN = [random(1,100) for i in range(n)]
    minN = 0
    minId = 0
    sum = listN[0]
    print(listN)
    for i in range(1, len(listN)):
        if listN[i] < listN[i-1]:
            minN = listN[i]
            minId = i
        sum += listN[i]
    sum = sum/len(listN)
    listN[minId] = sum
    print(listN)
        
lab2(5)