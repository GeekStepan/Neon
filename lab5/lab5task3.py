from random import randint as random

def lab3(n):
    listA = [random(1,100) for i in range(n)]
    x = random(1,100)
    minus = 100
    aX = str("0")
    print(listA, x, minus)
    for i in range(len(listA)):
        print(listA[i])
        for k in range(len(listA)):
            print(listA[k])
            if abs(x - ((listA[i]+listA[k])/2)) < minus and k!=i:
                minus = (x - (listA[i]+listA[k])/2)
                aX = str(listA[i])+str("+")+str(listA[k])
                print(aX)

lab3(5)