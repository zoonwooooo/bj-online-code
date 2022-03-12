a=input()
array=list(map(int,a))
array.sort(reverse=True)
print("".join(map(str,array)))

