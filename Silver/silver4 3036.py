def ec(a,b):
    while b != 0:
        r= a % b 
        a=b
        b=r
    return a
int(input())
li1=list(map(int,input().split()))
for i in range (1,len(li1)):
    c=ec(li1[0],li1[i])

    print(str(int(li1[0]/c))+"/"+str(int(li1[i]/c)))
