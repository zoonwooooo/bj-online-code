from collections import deque
import sys
deq_1=deque()
for _ in range(int(sys.stdin.readline().strip())):
    a=sys.stdin.readline().split()

    if a[0]=="push_back":
        deq_1.append(int(a[1]))
    if a[0]=="push_front":
        deq_1.appendleft(int(a[1]))
    if a[0]=="pop_front":
        if len(deq_1)==0:
            print(-1)
        else:
            print(deq_1.popleft())
    if a[0]=="pop_back":
        if len(deq_1)==0:
            print(-1)
        else:
            print(deq_1.pop())
    if a[0]=="size":
        print(len(deq_1))
    if a[0]=="empty":
        if len(deq_1)==0:
            print(1)
        else:
            print(0)
    if a[0]=="front":
        if len(deq_1)==0:
            print(-1)
        else:
            print(deq_1[0])
    if a[0]=="back":
        if len(deq_1)==0:
            print(-1)
        else:
            print(deq_1[-1])


