import itertools
import sys
from itertools import combinations
from re import A
import re
input = sys.stdin.readline
n,s=map(int,input().split())
array=list(map(int,input().split()))
k=0
for i in range(1,n+1):
    a=combinations(array,i)
    for x in a:
        if sum(x)==s:
            k+=1
print(k)