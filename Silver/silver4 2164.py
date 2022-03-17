from collections import deque
n=int(input())
deq_1=deque(i for i in range(1,n+1))
print(deq_1)
while True:
    deq_1.popleft()
    deq_1.append(deq_1[0])
    deq_1.popleft()

    if len(deq_1)==1:
        break

print(deq_1[0])