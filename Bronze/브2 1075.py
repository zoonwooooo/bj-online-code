N=(input())
F=int((input()))
for i in range(-2,0):
    posn = i
    nc = "0"
    tmp = list(N)
    tmp[posn] = nc
    N = "".join(tmp)
N=int(N)
K=F-(N%F)
if K==F:
    s=str(N)
    print(s[-2:])
else:
    s=str(N+K)
    print(s[-2:])
#입력받은 문자열->리스트->수정->수정된 리스트를->문자열->숫자