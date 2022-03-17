from collections import deque
n,k=map(int,input().split())
deq_1=deque(range(1,n+1))
deq_2=deque()

while True:
    if len(deq_1)==0:
        break
    deq_1.rotate(-k+1)
    deq_2.append(deq_1.popleft())

print('<'+', '.join(map(str,deq_2))+'>')

