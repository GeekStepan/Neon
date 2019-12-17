from random import randint as random

def lab6task1(x):
    listNum = [i for i in range(1, x+1)]
    #listNum = [random(1,100) for i in range(x)]
    matrixList = []
    print("\n")
    for i in range(x):
        matrixList.append([0] * x)
    print(listNum)
    print("\n")
    for i in range(x):
        print(matrixList[i])
    for i in range(x):
        for j in range(x):
            matrixList[i][j] = (listNum[j] ** (i+1))
    print("\n")
    for i in range(x):
        print(matrixList[i])
    
lab6task1(int(input("Введите размер матрицы: ")))