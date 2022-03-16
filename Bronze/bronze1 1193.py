x=int(input())
for n in range(100000):
    if n*(n-1)/2 < x <= n*(n+1)/2:
        num=n
        break
if num%2==0:
    num_1=int(x-n*(n-1)/2)
    b=num-num_1+1
    a=num+1-b
    print(str(a)+"/"+str(b))

else:
    num_1=int(x-n*(n-1)/2)
    b=num_1
    a=num+1-b
    print(str(a)+"/"+str(b))

