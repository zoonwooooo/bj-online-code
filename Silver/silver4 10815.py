import sys
n=int(input())
list_n=list(map(int,sys.stdin.readline().split()))
list_n.sort()
m=int(input())
list_m=(map(int,sys.stdin.readline().split()))
def fuct(target,data):
    start=0
    end=len(data)-1
    while start<=end:
        mid= (start + end)//2
        if target==data[mid]:
            return 1
        elif target > data[mid]:
            start=mid+1
        elif target < data[mid]:
            end=mid-1
    return 0

for i in list_m:
    if fuct(i,list_n)== 0:
        print("0",end=" ")
    elif fuct(i,list_n)== 1:
        print("1",end=" ")



