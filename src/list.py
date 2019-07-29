#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：zangfans time:2019/6/17
# l = [1,2,3]
# print(type(l))
#
# l1=list([1,2,3,4])
# print(type(l1))

#切片
# l=['a','b','c','d','e','f']
# print(l[1:5])
# print(l[1:5:2])
# print(l[2:5])
# print(l[-1])

# print(l[-1:-4])
# print(l[-4:])

#追加
# hobbies = ['play','eat','sleep','study']
# hobbies.append('girls')
# print(hobbies)


#删除
# hobbies1 = ['play','eat','sleep','study']
# x = hobbies1.pop()  #不是单纯的删除，是删除并且把删除的元素返回，我们可以用一个变量名去接收该返回值
# print(x)
# print(hobbies1)

# #队列：先进先出
# queue_l = []
# #入队
# queue_l.append('first')
# queue_l.append('second')
# queue_l.append('third')
# print(queue_l)
#
# #出队
# print(queue_l.pop(0))
# print(queue_l.pop(0))
# print(queue_l.pop(0))


# #堆栈：先进后出，后进先出
# stack_l = []
# stack_l.append('first')
# stack_l.append('second')
# stack_l.append('third')
#
# print(stack_l.pop())
# print(stack_l.pop())
# print(stack_l.pop())

#长度len
# hobbies = ['play','eat','sleep','study']
# print(len(hobbies))

#包含in
# hobbies = ['play','eat','sleep','study']
# count=0
# while True:
#     count += 1
#     s1 = input("please input your hobbies >")
#     if s1 in hobbies:
#         print("sucess")
#         print(count)
#         break

#insert指定位置插入
# hobbies=['play','eat','sleep','study','eat','read']
# hobbies.insert(1,'walk')
# hobbies.insert(1,['walk1','walk2','walk3'])
# print(hobbies)
#
# print(hobbies.count('eat'))     #查看字符出现的次数
#
# hobbies.extend(['walk1','walk2','walk3'])
# print(hobbies)


#apped和extend的区别
# x = [1,2,3]
# x.append([4,5])
# print(x)
#
# y = [1,2,3]
# y.extend([4,5])
# print(y)

# hobbies=['play','eat','sleep','study','eat','read']
#hobbies.clear()     #清空所有元素
#print(hobbies)

# l = hobbies.copy()   #复制所有元素
# print(l)

# l=[1,2,3,4,5]
# l.reverse()   #倒叙,反排
# print(l)
#
# l=[100,-1,200,-9,10]
# l.sort(reverse=True)
# print(l)




'''
字符串切片
切片操作（slice）可以从一个字符串中获取子字符串（字符串的一部分）。我们使用一对方括号、起始偏移量start、终止偏移量end 以及可选的步长step 来定义一个分片。

格式： [start:end:step]

[:] 提取从开头（默认位置0）到结尾（默认位置-1）的整个字符串
 [start:] 从start 提取到结尾
 [:end] 从开头提取到end - 1
 [start:end] 从start 提取到end - 1
 [start:end:step] 从start 提取到end - 1，每step 个字符提取一个
 左侧第一个字符的位置/偏移量为0，右侧最后一个字符的位置/偏移量为-1
'''


# def re_sort():
#     s = input('请输入一串字符串：>>')
#     return s[::-1]
# obj = re_sort()
# print(obj)
# print(type(obj))


def re_sort2():
    s = input('请输入一串字符串：>>')
    li = []
    for i in s:
        li.append(i)
    li.reverse()
    print(li)
    print(type(li))
    return ''.join(li)
obj2 = re_sort2()
print(type(obj2))


'''
可变数据类型和不可变数据类型
'''
#1.可变数据类型：在id不变的情况下，value可改变（列表和字典是可变类型，但是字典中的key值必须是不可变类型）

# l = [1,2,3]
# print(id(l))
#
# l[0] = 1111
# print((id(l)))
# print(l)


#2.不可变数据类型：value改变，id也跟着改变（数字，字符串，布尔类型，都是不可变类型）
# s = 'hello'
# print(id(s))
#
# s = 'world'
# print(id(s))

s = u'臧'
print(repr(s))
print(type(s))
print(s.encode('utf-8'))
print(s.encode('gbk'))







































