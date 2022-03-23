import sys
def facto(x):
    a=1
    for i in range(1,x+1):
        a=a*i
    return a

for _ in range(int(sys.stdin.readline())):
    n,m=map(int,sys.stdin.readline().split())
    print(facto(m)//facto(n)//facto(m-n))
