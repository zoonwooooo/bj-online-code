M=int(input(""))
dic={"A" : 1,
      "B" : 2,
      "C" : 3}
reverse_dic= dict(map(reversed,dic.items()))
for i in range(M):
    a,b = map(int,input("").split())
    t=reverse_dic[a]
    reverse_dic[a]=reverse_dic[b]
    reverse_dic[b]=t
rere_dic=dict(map(reversed,reverse_dic.items()))
print(rere_dic["A"])

