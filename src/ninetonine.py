#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：zangfans time:2019/12/19
#for循环是有规则的，while循环是无规则的


for i in range(1,10):
    for j in range(1,10):
        result = i * j
        print("%d*%d=%-2d  " %(i, j, result), end="")
    print()

n = int(input("请输入大于1的整数>  "))
if (n == 2):
    print("2 是质数！")
else:
    for i in (2, n):
        if (n % i == 0):
            print("%d 不是质数!" % n)
            break
        else:
            print("%d 是质数!" % n)

