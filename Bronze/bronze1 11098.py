import sys
for i in range(int(sys.stdin.readline())):  #테스트 개수
    array1=[]
    array2=[]
    for k in range(int(sys.stdin.readline())): #선수입력 횟수
        array1.append(sys.stdin.readline().split()) #선수 입력
    for i in range(0,len(array1)):
        array2.append(int(array1[i][0]))
    a=max(array2)
    b=array2.index(a)
    print(array1[b][1])
       
       
       


         


  


