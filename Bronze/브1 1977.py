M=int(input())
N=int(input())
i=1
array=[]
while True:
    if i**2 > N:
        break
    elif i**2>=M :
        array.append(i**2)
    i+=1
if sum(array) == 0:
    print(-1)
else:
    print(sum(array))
    print(array[0])


