a,b=input().split()
li1=[]
for i in range(len(b)-len(a)+1):
    count=0
    for i2 in range(len(a)):
        if a[i2]!=b[i2+i]:
            count+=1
    li1.append(count)

print(min(li1))


#idea) 주어진 두 문장을 비교해서 겹쳐진 개수가 최소인 값이 원하는 값의 최소