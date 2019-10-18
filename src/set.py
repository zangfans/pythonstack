#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：zangfans time:2019/6/19


set1 = {1,2,3,4,5}
set2 = {1,2,3,4,6}
print(set1 >= set2)


print(set1.issuperset(set2))    #父集
print(set1.issubset(set2))   #子集
print(set1.intersection(set2))   #交集
print(set1.union(set2))   #并集
print(set1.difference(set2))   #差集
print(set1.symmetric_difference(set2))   #对称差集


pythons = {'zf1','zf2','zf3','zf4','zf4','zf5','zf6'}
linuxs = {'zf4','zf7','zf5'}

print(pythons.intersection(linuxs))
print(pythons.union(linuxs))

python1 = pythons.intersection(linuxs)
print(pythons.difference(python1))

print(pythons.difference(linuxs))

print(pythons & linuxs)
print(pythons | linuxs)
print((pythons - linuxs))
print(pythons ^ linuxs)


linux = {'1','2','3'}
linux.add('4')  #说明set类型的集合是可变类型
print(linux)

#linux.add([1,2,3])    #报错，只能添加可变类型

#res = linux.pop()   #不用指定参数，随机删除，并且会有返回值
#print(res)

res = linux.remove('1')  #指定元素删除，元素不存在则报错，单纯的删除，没有返回值

res = linux.discard('5')  #指定元素删除，元素不存在则报错，单纯的删除，没有返回值

print(linux)

print(linux.copy())
print(linux.clear())

解压
a,*_={'zzz','sss','xxxx','cccc','vvv','qqq'}
print(a)







