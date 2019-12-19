#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：zangfans time:2019/6/17
info_dic = {'name':'zangfan','age':24,'gender':"male"}

# print(info_dict['name111111'])   #找不到则报错
# print(info_dict.get('name111',None))    #get方法找不到不报错，可以自己设定默认值
# print(info_dict.get('name',None))

#删除
# print(info_dic.pop(('name13333',None)))   #不存在报错

# print(info_dic.popitem())
# print(info_dic)

# info_dic['level']=10    #添加键值对
# print(info_dic)


# print(info_dic.keys())
# print(info_dic.values())
# print(info_dic.items())


# for k in info_dic.keys():
#     print(k,info_dic[k])
#     print(k)
# for val in info_dic.values():
#     print(val)

# for k,v in info_dic.items():
#     k,v = ('name','egon')
#     print(k,v)


dict1 = {"apple":50, "juice":25}
print(len(dict1))

dict2 = dict1.copy()
print(dict2)


print(dict1.get("apple"))

print("apple" in dict1)

print(dict1.clear())


dict2 = {"apple": 50, "juice": 25, "pear": 30}
dict2["banana"] = 45
dict2["watermalon"] = 65
listkey = list(dict2.keys())
listvalue = list(dict2.values())
for i in range(0,len(listkey)):
    print("%s 的价格是 %d 元" % (listkey[i], listvalue[i]))






















































