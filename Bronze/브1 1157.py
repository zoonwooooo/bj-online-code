from string import ascii_uppercase
alpha_list = list(ascii_uppercase)
alpha=input("알파벳 ")
alpha=alpha.upper() #전부 대문자 ZZA
alpha_list2=alpha_list
alpha_list2=[0 for i in range(len(alpha_list))]
k=0
for i in alpha_list:
    if alpha.count(i)>0:
        alpha_list2[k]=alpha.count(i)
        k+=1











