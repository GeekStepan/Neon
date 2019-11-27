Kost=int(input('введите kost: '))
i=1

for i in range(1,Kost):
    k=0 
    s=0
    d=i #для второго цикла
    amstor=i
    while i>=1:
        i=i//10 #делим нацело  
        k+=1
    while d!=0:
        ost=d%10 #остаток от деления 
        d=d//10 #целое 
        s=s+ost 
    if amstor==s**k:
        print('amstor=',amstor)
input()