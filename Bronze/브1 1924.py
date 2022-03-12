x, y = map(int, input().split())
array = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
big_dic = {1: 0,
           2: 4,
           3: 4,
           4: 1,
           5: 6,
           6: 3,
           7: 1,
           8: 5,
           9: 2,
           10: 0,
           11: 4,
           12: 2
           }
print(array[y%7-big_dic[x]])
