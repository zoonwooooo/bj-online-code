n=int(input())
if n==4 or n==7:
    print(-1)
else:   
    a=n//5
    if n%5==0:
        print(a)
    elif  n%5==1:
        print(a+1)
    elif n%5==3:
        print(a+1)
    elif  n%5==4:
        print(a+2)
    elif n%5==2:
        print(a+2)
