N=int(input())
m=0
for i in range(N):
    m+=(i*N+i)
print(m)

N*(N-1)+(N-1)+N*(N-2)+(N-2)