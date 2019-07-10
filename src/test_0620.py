#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：zangfans time:2019/6/20
from urllib.request import urlopen

#1.初始函数

'''
map函数和reduce函数的区别
①从参数方面来讲：
map()函数：
　　 map()包含两个参数，第一个是参数是一个函数，第二个是序列（列表或元组）。其中，函数（即map的第一个参数位置的函数）可以接收一个或多个参数。
reduce()函数：
    reduce() 第一个参数是函数，第二个是 序列（列表或元组）。但是，其函数必须接收两个参数。

②从对传进去的数值作用来讲：
map()是将传入的函数依次作用到序列的每个元素，每个元素都是独自被函数“作用”一次；
reduce()是将传人的函数作用在序列的第一个元素得到结果后，把这个结果继续与下一个元素作用（累积计算），最终结果是所有的元素相互作用的结果。
'''

# print(reduce(lambda x,y:sum([x,y]),range(1,101)))
#
# print(map(lambda x,y:sum([x,y]),range(1,101)))
#
# print(list(map(lambda x,y:sum([x,y]),range(1,101),range(1,101))))

# def length():
#     s = 'hello world'
#     length1 = 0
#     for i in s:
#         length1 += 1
#     return length1
# print(length())

#函数有一个和多个返回值
# def func1():
#     a = 111
#     b = [1,2,3]
#     c = {'a':15,'b':6}
#     return a,b,c   #返回多个值，变量之间按逗号隔开，以元组的形式返回
# print(func1())

#函数没有返回值的函数

#1.不写return时返回None
# def f1():
#     a = 11
#     b = [1.2]
# print(f1())
#
#
# #2.只写一个return时返回None
# def f2():
#     a = 11
#     b = [1,2]
#     return
# print(f2())
#
# #3.return None的时候返回None
# def f3():
#     a = 11
#     b = [1,2,3]
#     return None
# print(f3())
#
#
# #举例说明return的作用
#
# def f4():
#     a = 111
#     print(a)
#     return   #结束一个函数的运行
#     print(a)
# print(f4())


#定义一个列表，返回列表的最后一个值
#方法1
# def f5():
#     a = [1,2,311,21,25]
#     return  a[-1]
# print(f5())

#方法2
# def f6():
#     l1 = ['hello','kitty',2019,6]
#     return l1
# m,n,k,g = f6()
# print(g)


# def fun(s):     #参数接受：形式参数，简称形参
#     '''
#     计算字符串长度的函数-------函数的功能
#     参数s：接受要计算的字符串------参数的信息
#     return：要计算字符串长度-------返回值得信息
#     '''
#     length = 0
#     for i in s:
#         length += 1
#         return length
# res = fun("helloworld")
# print(res)

'''
1.实参和形参
形参：是函数定义时候定义的参数
实参：函数调用的时候传进来的参数
'''

'''
2.传递多个参数
可以传递多个参数，多个参数之间用逗号隔开
站在传参的角度上，调用函数时传参数有两种方式：
    1.按照位置传递参数
    2.按照关键字传递参数
用法：
    1.位置参数必须在关键字参数的前面
    2.对于一个参数只能赋值一次
'''
# def compare_max(a,b):
#     if a > b:
#         return a
#     else:
#         return b
# a = input("please input a number:  ")
# b = input("please input a number:  ")
#
# print(compare_max(a,b))

# print(compare_max(20,30))   #1,按照位置传递参数
# print(compare_max(a=10,b=30))  #2,按照关键词传递参数
# print(compare_max(10,b=30))    #3,位置和关键字传参混搭

'''
3.默认参数
用法：为什么使用默认参数？将变化比较小的值设置成默认参数
定义：默认参数可以不传，不传时用的就是默认值，如果带参数就会覆盖默认值
    默认的值是在定义函数的时候就已经确定了的
'''
# def stu_info(name,sex="male"):
#     print(name,sex)
# stu_info('zangfan')
# stu_info('beibei','female')


#默认参数缺陷：默认参数是一个可变的数据类型
# def defaul_param(a,l=[]):
#     l.append(a)
#     print(l)
# defaul_param('my name is')
# defaul_param('zangfan')

'''
4.动态参数
按位置传值多余的参数都由args统一接收，保存成一个元组的形式
按关键字传值接收多个关键字参数，由kwargs接收，保存成一个字典的形式
'''
#*args的应用
# def fun(a,b,*args):
#     sum = a+b
#     for i in args:
#         sum += i
#     return sum
# print(fun(2,3,3))

#*kwargs的应用
# def func(*args,**kwargs):
#     print(args,kwargs)
#
# func(10,20,ccc=10,ddd=10,eee=1000)



'''
函数嵌套及作用域
'''

#1.三元运算
# a = 10
# b = 20
# c =a if a > b else b
# print(c)


#2.命名空间
#全局命名空间：创建的存储“变量名与值的关系”的空间



'''

'''
# def func1():
#     a = 2
#     b = 4
#     print(locals())
#     print(globals())
# func1()



#global关键字：强制转换为全局变量
# x = 1
# def foo():
#     global x    #强制转换x为全局变量
#     x = 1000000
#     print(x)
# foo()
# print(x)   #1000000  这个方法能少用就少用


#nonlocal让内部函数中的变量在上一层函数中生效，外部必须有
# x = 1
# def f1():
#     x = 2
#     def f2():
#         #x = 3
#         def f3():
#             #global x
#             nonlocal x
#             x = 10000
#         f3()
#         print('f2内的打印',x)
#     f2()
#     print('f1内的打印',x)
# f1()
# print(x)

#函数的嵌套定义
# def animal():
#     def tiger():
#         print('nark')
#         print('eat')
#     tiger()
# animal()


#函数得作用域链
# x = 1
# def f1():
#     x = 'h'
#     def inner():
#         x = 'w'
#         def inner2():
#             print(x)
#         inner2()
#     inner()
# f1()




#函数名的本质：就是函数的内存地址
# def func():
#     print('func')
# print(func)


#函数名可以用做函数的参数
# def func():
#     print('func')
# def func2(f):
#     f()
# func2(func)

#函数名可以作为函数的返回值
# def func():
#     def func3():
#         def func4():
#             print('func4')
#         return func4
#         print('func3')
#     return func3
# f2 = func()
# f2()

# def f1(x):
#     print(x)
#     return '123'
#
# def f2():
#     ret = f1('s')  #f2作为调用函数
#     print(ret)
# f2()


# def func():
#     def func2():
#         return 'a'
#     return func2    #函数名作为返回值
#
# func2 = func()
# print(func2())


#闭包
#1.闭：内部的函数
#2.包：包含了对外部函数作用域中变量的引用
# def f1():
#     x = 20
#     def f2():
#         x = 10
# print(x)

# 闭包的常用形式：
# def hei():
#     x=20
#     def inner():
#         '''闭包函数'''
#         print(x)
#     return inner()
# hei()



#判断闭包函数的方法
#输出的_closure_有cell元素：是闭包函数
# def func():
#     name = 'eva'
#     def inner():
#         print(name)
#     print(inner.__closure__)
#     return inner()
#
# f = func()
# f

#输出的_closure_为None：不是闭包函数
name = 'egon'
def func2():
    def inner():
        print(name)
    print(inner.__closure__)
    return inner
f2 = func2()
f2


#闭包获取网络应用
def index(url):
    def inner():
        return urlopen(url).read()
    return inner
u = 'http://www.cnmo.com'
get = index(u)
print(get())

####总结
#作用域：小范围的可以用大范围的，单是大范围的不能用小范围的，范围从大到小
















