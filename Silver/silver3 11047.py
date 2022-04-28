a,b=map(int,input().split())
list_1=[]
count=0
for _ in range(a):
    list_1.append(int(input()))
list_1.reverse()

for i in list_1:
    if i<=b:
        count+=b//i
        b=b%i

print(count)
