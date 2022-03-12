n=2
while True:
    a=input()
    if "Was it a cat I saw?" ==a:
        break
    for i in range(0,len(a),n):
        print(a[i],end="")
    print()
    n += 1





