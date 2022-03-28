import sys
a={}
for _ in range(int(sys.stdin.readline())):
    str1=sys.stdin.readline().strip()
    if str1 in a:
        a[str1]+=1
    if str1 not in a:
        a[str1]=1

b=([k for k,v in a.items() if max(a.values()) == v]) 
b.sort()
print(b[0]) 
