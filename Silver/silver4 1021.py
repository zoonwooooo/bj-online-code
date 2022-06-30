import sys
from collections import deque
m,n=sys.stdin.readline().split()
deque_1=deque([i for i in range(1,int(m)+1)])
count=0
list_1=list(map(int,sys.stdin.readline().split()))
print(list_1)
for num in list_1:
    while True:
        if deque_1[0]==num:
            deque_1.popleft()
            break

        else:
            if deque_1.index(num) <= len(deque_1)//2:
                deque_1.rotate(-1)
                count+=1
            else:
                deque_1.rotate(1)
                count+=1
                    
print(count)