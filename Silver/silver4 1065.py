n=int(input())
array=[]
count=0
for i in range(100,n+1):
   array.append(i)
   array=list(map(str,array))
if n==1000:
    n=999
if n<100:
    count=n
if n>=100:
    for i in range(0,n-99):
        a=array[i]
        if int(a[0])-int(a[1])==int(a[1])-int(a[2]):
            count+=1
    count=count+99
print(count)

