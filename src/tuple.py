#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：zangfans time:2019/6/17
# t1=(1,[1,2],'sss',(1,2))
# t2=tuple((1,[1,2],'sss',(1,2)) )
# print(t1)
# print(t2)
#
# print(type(t1))
# print(type(t2))
#
# goods = ('iphone','lenovo','samsung','sony')
# print(goods[1:3])
# print('lenovo' in goods)
#
# d1 = {'a':1,'b':2,'c':3}
# print('b' in d1)   #查看key为b在不在d1字典里面

# goods = ('iphone','lenovo','samsung','sony')
# print(goods.index('iphone'))
# print(goods.count('iphone'))

#补充：元组本身是不可变的，但是内部的元素可以是可变类型
t = (1,['a','b'],'sss',(1,2))
# t = tuple((1,[1,3]),'sss',[1,2])

t[1][0]='A'
print(t)
t[1][0]='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
print(t)


#元祖类型数据更改方法：把元组数据转换为列表赋予一个新对象，在进行更改
tuple4=(1,2,3,4)
list4 = list(tuple4)
print(list4)
list4.append(5)
print(list4)
































