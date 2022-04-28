a=int(input())
list_1=list(map(int,input().split()))
list_1.sort()
zero=0

for i in range(a):
   zero+=list_1[i]*(a-i)

print(zero)