n=int(input())
dic={}
for i in range(n):
    dic[i]=tuple(map(int,input().split())),0
for i1 in range(len(dic)-1):
    a=dic[i1]
    for i2 in range(1,len(dic)):
        b=dic[i2]
        if i1 < i2:
            if a[0][0] < b[0][0] and a[0][1] < b[0][1]:
                dic[i1][1]=dic[i1][1]+1
            if a[0][0] > b[0][0] and a[0][1] > b[0][1]:
                dic[i2][1]=dic[i2][1]+1
for i in range(len(dic)):
     print(dic[i][1]+1,end=" ")

    