from itertools import permutations
n,m=map(int,input().split())
list_1=[]
for _ in range(1,n+1):
    list_1.append(_)
for i in permutations(list_1,m):
    for i2 in range(m):
        print(i[i2],end=" ")
    print()