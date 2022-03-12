n,s=map(int,input().split())
array=list(map(int,input().split()))
k=0
for i in range(n):
    if sum(array[0:i])==s:
        k+=1
for i in range(n):
    if sum(array[0:i])==s:
        k+=1
for i in range(n):
    if sum(array[0:i])==s:
        k+=1
for i in range(n):
    if sum(array[0:i])==s:
        k+=1
print(k)

def fuct(x):
    if sum(array[x:i])==s:
        k+=1