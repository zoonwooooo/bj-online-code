import sys
a=[]
for _ in range(int(sys.stdin.readline())):
    a.append(sys.stdin.readline().strip())
b=set(a)
a=list(b)
a.sort()
a.sort(key=len)
print("\n".join(a))




