import sys
n=int(sys.stdin.readline())
array1=list(map(int,sys.stdin.readline().split()))
array1=set(array1)
array1=list(array1)
array1.sort()
print(" ".join(map(str,array1)))