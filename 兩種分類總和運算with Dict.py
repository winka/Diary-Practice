# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 12:05:32 2023

@author: winka
"""

# 算出兩個分類的總和 group1 & group2

dict1 = {'key1':5,
         'key2':5,
         'key3':5,
         'key4':5,
         'key5':5,
         'key6':5,
         'key7':5}

# 分類
count_list = [('key1','key2','key3','key4'),('key5','key6','key7')]

# print(count_list[0])
dict2 ={'group1':0,
        'group2':0}
# 計算
for key,value in dict1.items(): 
    for i in range(2):
        if i==0 and key in count_list[i] :
            dict2['group1'] = dict2['group1'] + dict1[key] 
        elif i==1 and key in count_list[i] :
            dict2['group2'] = dict2['group2'] + dict1[key] 
            
            
print(dict2)