def Armstrong(x):
    bigList = [i for i in range(1, x+1)]
    armstrongList = []
    sumX = 0
    for i in bigList:
        sumX = 0
        xNum = map(int, str(i))
        xNum = list(xNum)
        for j in range(len(xNum)):
            sumX += int(xNum[j])
        print("\nСумма цифр равна: ", sumX)
        print("i = ", i, "sumX^n = ", sumX ** len(xNum))
        if sumX ** len(xNum) == i:
            armstrongList.append(i)
    print(armstrongList)

x = int(input("Введите число: "))
Armstrong(x)