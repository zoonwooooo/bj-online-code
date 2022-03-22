for _ in range(int(input())):
    array1=list(map(str,input().split()))
    for i in range(len(array1)):
        print(array1[i][len(array1[i]): :-1],end=" ")
