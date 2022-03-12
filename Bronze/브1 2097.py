N=int(input())
k=N ** 0.5
i=3
if N==1 or N==2 :
    print(4)
elif k==int(k):
    print((int(k)-1)*4)
else:
    while True : # N=7
        if (i)**2>N>(i-1)**2: #i값 구함 i =3
            m=int(((i) ** 2 - (i - 1) ** 2 - 1 )/ 2) #둘사이 거리 4  6  8 10
            if (i)**2>N>=(i)**2-m:
                print((int(i)-1)*4)
            else:
                print((int(i)-1)*4-2)
            break
        else:
            i+=1