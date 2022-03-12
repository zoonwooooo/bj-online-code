#x%n==x//n
#N= X%N+ X//N
N=int(input("N")) #3
i=1
array=[]
while True:
    if  i%N == i//N :
        array.append(i)
    if len(array)==N-1:
        break
    i+=1
print(sum(array))


