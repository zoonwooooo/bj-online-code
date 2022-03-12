N=int(input())
for i in range(N):
    array=input().split()
    a=float(array[0])
    for i in array:
        if "#" in i:
            a=a-7
        elif "%" in i:
            a=a+5
        elif "@" in i:
            a=a*3
        else:
            pass
    print("{:.2f}".format(a))


