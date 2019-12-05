from random import randint as random

def good(x):
    listNum = [random(1,100) for i in range(1, x+1)]
    print(listNum)
    n = 1
    for i in range(len(listNum)-1):
        if listNum[i+1] <= listNum[i]:
            print("")
            n = 0
            break

    if n == 1:
        print("Последовательность возрастающая")
    
    else:
        print("Последовательность не возрастающая")

good(3)

