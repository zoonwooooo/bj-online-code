t=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
sum=0
for i in range(len(a)):
    sum+=max(b)*a[i]
    b.remove(max(b))
print(sum)