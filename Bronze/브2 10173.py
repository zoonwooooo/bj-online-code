#리스트 내부의 요소들을 대문자로 바꿔주고싶으면
#새로운 리스트에 요소를 UPPER함수를 사용해 대문자를 만들어서 사용한다
array=[]
while True:
    array.append(input().upper())
    if "EOI" in array:
        break
del array[-1]
for i in array:
    if "NEMO" in i:
        print("Found")
    else:
        print("Missing")

