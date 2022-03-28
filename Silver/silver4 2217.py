import sys
n=int(int(sys.stdin.readline().strip()))
array1=[]
max_1=0
for _ in range(n):
    array1.append(int(sys.stdin.readline().strip()))
array1.sort()
for i in range(n):
    if array1[i]*(n-i) > max_1:
        max_1=array1[i]*(n-i)
print(max_1)