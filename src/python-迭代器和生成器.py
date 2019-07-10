#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：zangfans time:2019-7-2
from collections.abc import Iterable
from collections.abc import Iterator

'''
一、可迭代协议：可以被迭代要满足要求的就叫做可迭代协议。内部实现了_iter_方法
iterable：可迭代的一一对应的标志
什么叫迭代？：一个一个取值，就像for循环一样取值
字符串，列表，元组，集合，字典都是可迭代的

'''


'''
二、迭代器协议：内部实现了_iter_，_next_方法
迭代器大部分都是在python的内部去使用的，我们直接拿来用就行了
迭代器的优点：如果用了迭代器，节约内存，方便操作
dir([1,2]._iter_())是列表迭代器中实现的所有的方法，而dir([1,2])是列表中实现的所有方法，都是以列表的方式返回给我们
为了方便看清楚，我们把他们转换成集合，然后取差集，然而，我们看到列表迭代器中多出了三个方法，那么这三个方法都分别是干什么的呢？
'''

# print(dir([1,2].__iter__()))    #查看列表迭代器的所有方法
# print(dir([1,2]))   #查看列表的所有方法
# print(set(dir([1,2].__iter__()))-set(dir([1,2])))

# iter_l = [1,2,3,4,5,6].__iter__()
# print(iter_l.__length_hint__())   #获取迭代器中元素的长度
# print(iter_l.__setstate__(4))#根据索引指定从哪里开始迭代
#
# print(iter_l.__next__())    #一个一个的取值
# print(iter_l.__next__())
# print(iter_l.__next__())

# print(next(iter_l))

#next(iter_l)和iter_l.__netx__()方法一样，推荐使用next(iter_l)

# l = [1,2,3,4,5]
# a = l.__iter__()

# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
#上面的列表长度只有5个，而你多打印了就不会报错。处理的情况如下，就不会报错


# while True:
#     try:
#         item = a.__next__()
#         print(item)
#     except StopIteration:   #异常处理
#         break

#三、可迭代和迭代器的相同点：都可以用for循环

#四、可迭代和迭代器的不同点：就是迭代器内部多实现了一个_next_方法

#五、判断迭代器和可迭代的方法
#第一种：判断内部是不是实现了__next__方法

#第二种：
    #iterable  判断是不是可迭代对象
    #iterator  判断是不是迭代器

# Iterable ：故名思议，实现了这个接口的集合对象支持迭代，是可迭代的。able结尾的表示 能...样，可以做...。
# Iterator:   在英语中or 结尾是都是表示 ...样的人 or ... 者。如creator就是创作者的意思。这里也是一样：iterator就是迭代者，我们一般叫迭代器，它就是提供迭代机制的对象，具体如何迭代，都是Iterator接口规范的。

#用法：
# s = '111'
# print(isinstance(s,Iterable))  #isinstance判断类型
# print(isinstance(s,Iterator))


#判断range函数和map函数

map1 = map(abs,[1,-1,3,5])
print(isinstance(map1,Iterable))
print(isinstance(map1,Iterable))

s = range(100)
print(isinstance(s,Iterable))
print(isinstance(s,Iterable))



































