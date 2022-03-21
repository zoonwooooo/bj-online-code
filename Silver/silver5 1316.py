count=0
for i in range(int(input())): 
    str_1=list(input())
    set_1=set(str_1) 
    if len(set_1)==1:  
        count+=1
    if len(set_1) >1 : 
        count2=0
        count3=0
        for i in set_1: # ab   8 1
            rest_list = list(filter(lambda x: str_1[x] == i, range(len(str_1))))
            if len(rest_list) > 1:
                for i2 in range(len(rest_list)-1):
                    if rest_list[i2+1]-rest_list[i2]==1:
                        count3+=1
                        if count3==len(rest_list)-1:
                            count2+=1
            if len(rest_list) ==1: 
                count2+=1
            if count2==len(set_1):
                count+=1
            
print(count)