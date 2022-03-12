def Rev(M):
    K="".join(map(str,M))
    M=int(K[::-1])
    return M
X,Y=input().split()
L=Rev(X)+Rev(Y)

print(Rev(str(L)))



