import random
import copy
array=[]
array2=[]
for i in range(8+1):
    array.append(int(input()))
while True:
    array1=copy.deepcopy(array)
    sample=random.sample(array1, 2)
    for i in range(0,1+1):
       array1.remove(sample[i])
    if sum(array1)==100:
        for i in range(7):
         print(sorted(array1)[i])
        break










