from random import randint as random

def lab5(n):
    #генерация случайного массива длинной n
    listA = [random(0, 1000) for i in range(n)] 
    #проверка частного случая   (длинна списка 5)
    #listA = [3, 5, 19, 0, 63] 
    #проверка другого частного случая (длинна списка 8)
    #listA = [3, 5, 0, 19, 0, 0, 0, 63] 
    #minA - минимальное число списка, sumA - сумма элементов, minID - ID минимального элемента
    minA = 0; sumA = 0; minID = listA[0] 
    print(listA)
    for i in range(1, n):
        if listA[i-1] >= listA[i]:
            minA = listA[i]
            minID = i
        sumA += listA[i]
    print("Минимальный элемент: ", minA)
    print("ID элемента: ", minID)
    sumA = sumA/len(listA)
    print("Среднее арифметическое все чисел:", sumA)
    listA[minID] = int(sumA)
    print(listA)

lab5(int(input("введите длину массива: ")))

