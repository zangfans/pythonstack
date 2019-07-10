#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：zangfans time:2019/6/20

'''
计算机可以进行的运算有很多种，不只是加减乘除，它和我们人脑一样，也可以做很多运算。

种类：算术运算，比较运算，逻辑运算，赋值运算，成员运算，身份运算，位运算，今天我们先了解前四个。
'''

# print(11 != 22)
#
#
#
# print(1 > 2 and 1<2)
# print(1 > 2 or 1<2)
# print(not 1 > 2)


############break循环和continue循环的区别
#break循环结束本层循环
#continue结束本层循环

count = 0
while count < 10:
    if count >= 4 and count <= 6:
        count += 1
        #continue
        break
    print(count)
    count += 1























