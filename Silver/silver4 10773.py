from collections import deque
import sys
deq_1=deque()
for _ in range(int(sys.stdin.readline().strip())):
    n=int(sys.stdin.readline().strip())
    if n==0:
        deq_1.pop()
    else:
        deq_1.append(n)
print(sum(deq_1))