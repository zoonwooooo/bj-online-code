dict={0:0,1:1}
z=0

def fi(n):
    global z
    if n in dict:
        return dict[n]
    else:
        output=fi(n-1)+fi(n-2)
        dict[n]=output
        return dict[n]

T=int(input())

for i in range(T):
    a=int(input())
    print(z,fi(a))
    zero=0

