import sys
a,b=sys.stdin.readline().split()
set_a=set()
set_b=set()
for _ in range(int(a)):
    set_a.add(sys.stdin.readline().strip())

for _ in range(int(b)):
    set_b.add(sys.stdin.readline().strip())

a=list(set_a.intersection(set_b))
a.sort()
print(len(a))
for i in range(len(a)):
    print(a[i])

