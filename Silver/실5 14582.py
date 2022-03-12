a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in range(9):
    A=a[0:i+1]
    B=b[0:i+1]
    if a[0]>0:
        print("Yes")
        break
    elif sum(A)>sum(B) or sum(A)>sum(b[0:i]) :
        print("Yes")
        break
if sum(A)<=sum(B) and sum(A)<=sum(b[0:i]) :
    print("No")


