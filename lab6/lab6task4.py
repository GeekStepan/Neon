def lab6task4(x):
    n = 1
    matrixList = [[0 for i in range(x)] for i in range(x)]
    for i in range(x):
        print(matrixList[i])

    for i in range(x):
        for j in range(x):
            matrixList[i][j] = n
            n += 1

    for i in range(x):
        print(matrixList[i])

lab6task4(5)

