n,m=map(int,input().split())
array=list(map(int,input().split()))
right=1
left =0
k=0
while right <= n and left <= right:
    a=array[left:right]
    sum_sum=sum(a)
    if sum_sum==m:
        k+=1
    elif sum_sum<m:
        right+=1
    else:
        left+=1
print(k)
