from random import randint as random

def lab3(x):
    #listA = [int(random(1, 1000)) for i in range(random(1, 100))]; n = random(1, 10000)
    #listA = [10, 2, 32, 24, 8, 64, 7, 25, 23, 53]; n = x
    listA =[100, 3, 0, 1, 32, 28, 512, 3, 87, 17, 6, 3, 97, 5]; n = x
    print(listA, "\n")
    strA = str("0")
    test1 = 0; test2 = 0
    for i in range(len(listA)):
        for k in range(len(listA)):
            if i != k and abs(x - ((listA[i]+listA[k])/2)) < n:
                n = abs(x - ((listA[i]+listA[k])/2))
                test1 = listA[i]; test2 = listA[k]
                strA = str(listA[i]) + str(" + ") + str(listA[k])
                print(x, " - ", (listA[i]+listA[k])/2, " = ", abs(x - ((listA[i]+listA[k])/2)))
                print(strA, "среднее арифметическое: ", ((test1+test2)/2), "\n")

lab3(int(input("x = ")))

