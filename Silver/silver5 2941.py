from re import A


array=["c=","-c","dz=","d-","lj","nj","s=","z="]
a= input()

for t in array:
    a = a.replace(t,"*")

print(len(a))