from itertools import combinations
a,b=map(int,input().split())
list_1=[i for i in range(1,a+1)]

for i in combinations(list_1,b):
    for i2 in i:
        print(i2,end=' ')

    print()