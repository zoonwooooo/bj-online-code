num_1=input("")
count=0
if 0<=int(num_1)<10:
    num_1="0"+num_1
n=num_1
num_2=str((int(num_1[0])+int(num_1[1]))%10)
while True:
    num_1=num_1[1]+num_2
    num_2=str((int(num_1[0])+int(num_1[1]))%10)
    count+=1
    
    if num_1==n:
        break
print(count)


