import sys
set_1=set()
for i in range(int(sys.stdin.readline())):
    set_1.add(int(sys.stdin.readline()))
for i in sorted(set_1):
    print(i)