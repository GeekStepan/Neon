#Составить программу нахождения наименьшего общего кратного трех натуральных чисел.
def number(num1, num2, num3):
    numLs = [i for i in range(num1,(num1*num2*num3)+1)]
    for i in numLs:
        if (i%num1 == 0) and (i%num2 == 0) and (i%num3 == 0):
            print("наименьшое общее кратное: ", i)
            break

n1 = 9; n2 = 10; n3 = 4
number(n1, n2, n3)