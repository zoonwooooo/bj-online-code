from array import array
from collections import deque
from re import T
import sys
for i in range(int(sys.stdin.readline())):
    deq_3=deque()
    n,m=map(int,sys.stdin.readline().split())
    deq_1=deque(range(n))
    deq_2=deque(map(int,sys.stdin.readline().split()))

    while 1:
        if max(deq_2)==deq_2[0]:
            deq_3.append(deq_1.popleft())
            deq_2.popleft()
        elif max(deq_2)!=deq_2[0]:
            deq_1.rotate(-1)
            deq_2.rotate(-1)
        
        if len(deq_2)==0:
            print(deq_3.index(m)+1)
            break
