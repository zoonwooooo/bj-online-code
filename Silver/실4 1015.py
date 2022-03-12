N=int(input())
A=list(map(int,input().split()))
B=sorted(A)
p=[]
for i in range(len(B)):
     x=B.index(A[i])
     p.append(x)
     B[x]=-1
print(" ".join(map(str,p)))


