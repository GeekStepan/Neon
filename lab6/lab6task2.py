from random import randint as random

def lab6task2(x):
    randomMatrix = [[random(-100, 100) for i in range(x)] for i in range(x)]
    print("\n")
    for i in range(x):
        print(randomMatrix[i])

    for i in range(x):
        for j in range(x):
            if randomMatrix[i][j] > 0:
                randomMatrix[i][j] = 1
            elif randomMatrix[i][j] < 0:
                randomMatrix[i][j] = 0
    print("\n")
    for i in range(x):
        print(randomMatrix[i][0:i+1])

lab6task2(int(input("Введите размер матрицы: ")))
