import sys
for i in range(int(sys.stdin.readline().strip())):
    a=sys.stdin.readline().strip()
    a=a[::-1]
    num1,num2=0,0
    if len(a)%2!=0:
        print("NO")
    else:
        for m in a:
            if num2>num1:
                print("NO")
                break
            if m == ")":
                num1+=1
            elif m == "(":
                num2+=1

        if num1==num2:
            print("YES")
        elif num2<num1:
            print("NO")


            



    