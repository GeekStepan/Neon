from random import randint as random

def lab6task3(x):
    miniMatrix = [[random(1,99) for i in range(x)] for i in range(x)]
    minNum = 100; minId = 0; minSum = 0
    print("\n")
    for i in range(x):
        print(miniMatrix[i])

    for i in range(x):
        for j in range(x):
            if miniMatrix[i][j] < minNum:
                minNum = miniMatrix[i][j]
                minId = i

    print("\nСтрока: ", minId+1, "\nМинимальный элемент: ", minNum)
    print("\n")
    for i in range(x):
        print(minSum, "+", miniMatrix[minId][i], "=", minSum + miniMatrix[minId][i])
        minSum += miniMatrix[minId][i]
    print("Сумма равна: ", minSum)
    print("\n")
lab6task3(5)
