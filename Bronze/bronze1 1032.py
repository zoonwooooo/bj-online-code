n=int(input())
list1=list(input())

for i in range(n-1):
    list2=list(input())
    for i2 in range(len(lsit1)):
        if list1[i2]!=list2[i2]:
            list1[i2]="?"

print("".join(list1))