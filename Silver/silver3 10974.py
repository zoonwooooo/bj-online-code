from itertools import permutations
list1=[]
n=int(input())
for _ in range(1,n+1):
    list1.append(_)

for i in permutations(list1,n):
    for i2 in i:
        print(i2,end=" ")
    print()