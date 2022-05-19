def sum_1(n):
    f = [1,2,4]
    if n <=3:
        return f[n-1]
    else:
        for i in range(4, n+1):
            f.append(f[i-2] + f[i-3]+ f[i-4])
        return f[-1]

t=int(input())

for _ in range(t):
    k=int(input())
    print(sum_1(k))