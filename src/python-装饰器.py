#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：zangfans time:2019-7-2
import time



'''
1.为什么要使用装饰器呢？
装饰器的功能：在不修改源函数及其调用方式的情况下对源函数功能进行扩展
装饰器的本质：就是一个闭包函数

'''
#简单实例1
# def timmer(func):
#     def inner():
#         start = time.time()
#         func()
#         end = time.time()
#         print(end-start)
#     return inner
# def haha():
#     time.sleep(1)
#     print('sdjflsj')
# haha = timmer(haha)
# haha()

#上面的功能有点不简洁，不完美，下面引进了语法糖

# def wrapper(func):
#     def inner():
#         start = time.time()
#         func()
#         end = time.time()
#         print(end-start)
#     return inner
#
# @wrapper
# def kkk():
#     print('sjdfls')
# kkk()


#以上的装饰器都是不带参数的函数，现在装饰一个带参数的函数该怎么办呢？
#1，原函数带一个参数的装饰器


#2，原函数带多个参数的装饰器
# def timer(func):
#     def inner(*args,**kwargs):
#         start = time.time()
#         re = func(*args,**kwargs)
#         end = time.time()
#         print(end-start)
#         return re
#     return inner
#
# @timer
# def func1(a,b):
#     print('in func1')
#     print(a,b)
#
# @timer
# def func2(a):
#     print('in func2 and get a:%s'%(a))
#     return 'func2 over'
#
# func1(1,2)
# print(func2('aaaaa'))

#3，带返回值的装饰器
# def timer(func):
#     def inner(*args,**kwargs):
#         start = time.time()
#         re = func(*args,**kwargs)
#         end = time.time()
#         print(end-start)
#         return re
#     return inner
# @timer
# def jjj(a):
#     print('in jjj and get a:%s'%(a))
#     return 'fun2 over'
# jjj('aaaaaa')
# print(jjj('bbbb'))


#二、开放封闭原则
#1.对扩展是开放的
#2.对修改是封闭的

#三、装饰器的固定结构
# def wrapper(func):
#     def inner(*args,**kwargs):
#         '''函数执行之前的内容扩展'''
#         ret = func(*args,**kwargs)
#         return ret
#     return inner
#
# @wrapper
# def aaa():
#     time.sleep(1)
#     print('sjflsjdl')
#
# aaa()

#带参数的装饰器
#带参数的装饰器：就是给装饰器传参
#用处：就是当加了很多装饰器的时候，现在忽然有不想加装饰器了，想把装饰器去掉，但是那么多的代码，一个一个的去除很麻烦，因此我们可以利用带参数的装饰器去装饰它，它就像一个开关一样，要的时候就调用了，
#不用的时候就去掉了。给装饰器里面传个参数，那么那个语法糖也要带个括号。在语法糖的括号内传参。在这里我们可以用三层嵌套，弄一个标识去标识
# F = True  #为True是就把装饰器给加上了
# # F = False  #为False时就把装饰器给去掉了
# def outer(flag):
#     def wrapper(func):
#         def inner(*args,**kwargs):
#             if flag:
#                 print('before')
#                 ret = func(*args,**kwargs)
#                 print('after')
#             else:
#                 ret = func(*args,**kwargs)
#             return ret
#         return inner()
#     return wrapper
#
# @outer(F)
# def hahaha():
#     print('hahaha')
#
# @outer(F)
# def zang():
#     print('zangzang')
#
# hahaha
# zang


#多个装饰器装饰一个函数
# def qqqxing(fun):
#     def inner(*args,**kwargs):
#         print('in qqxing:before')
#         ret = fun(*args,**kwargs)
#         print('in qqxing:after')
#         return ret
#     return inner
#
# def pipixia(fun):
#     def inner(*args,**kwargs):
#         print('in qqxing:before')
#         ret = fun(*args,**kwargs)
#         print('in qqxing:after')
#         return ret
#     return inner
# @qqqxing
# @pipixia
# def dapangxie():
#     print('饿了么')
# dapangxie()


#统计多少个函数被我装饰了
l = []
def wrapper(fun):
    #l.append(fun)   #统计当前程序中有多少个函数被装饰了
    def inner(*args,**kwargs):
        l.append(fun)  #统计本次程序执行有多少个带有装饰器的函数被调用了
        ret = fun(*args,**kwargs)
        return ret
    return inner

@wrapper
def f1():
    print('in f1')

@wrapper
def f2():
    print('in f2')

print(l)








