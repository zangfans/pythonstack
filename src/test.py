#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：zangfans time:2019/4/4

# for i in range(5):
#     print("hello world!")
#
# print(13/8)
# x = 10
# y = 11
# if x > 9:
#     if y >10:
#         print(x+y)
#
# str1="hello world"
# print(len(str1))
import time


def compare_value(x,y):
    if (x > y):
        print(x,"is \033[31mhigh\033[0m",y)
    elif (x == y):
        print(x,"is \033[31mequal\033[0m",y)
    else:
        print(x,"is \033[31mlow\033[0m",y)
def sum(x,y):
    sum=(x+y)*y/2
    print(sum)

def sub(x,y):
    result = 0
    for i in range(x,y):
        result -= i
    return result

def multi(x,y):
    result = 1
    for i in range(x,y):
        result *= i
    return result

def div(x,y):
    result = 1
    result = x / result
    for i in range(x,y):
        result /= i

    return float(result*x)

if __name__ == '__main__':
    # x = input("please input a number:   ")
    # y = input("please input a number:   ")
    # compare_value(x,y)
    #sum(1,10)
    # sub(1,10)
    # multi(1,10)
    a=time.time()
    print(a)



