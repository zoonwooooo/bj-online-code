array=[]
for i in range(1,46+1):
    for i2 in range(i):
        array.append(i)
a,b= map(int,input().split())
print(sum(array[a-1:b]))