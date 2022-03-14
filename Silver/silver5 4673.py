a=set(range(1,10000))
b=set()
for i in a:
    for n in str():
        i+=int(n)
        b.add(i)
c=a-b
for k in sorted(c):
    print(k)