#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：zangfans time:2019/10/24

class Orange():
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Created")

#创建Orange类的实例
or1 = Orange(10, "dark orange")
or2 = Orange(4, "light orange")
#打印的是这是一个Orange对象
#print(or1)


#使用语法[对象名].[变量名] = [新的值]改变实例变量的值

print(or1.weight, or1.color)
print(or2.weight, or2.color)

class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len

    def change_size(self, w, l):
        self.width = w
        self.len = l

rectangle = Rectangle(10, 20)
print(rectangle.area())
rectangle.change_size(20, 40)
print(rectangle.area())


class shape():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print('''{} by {} '''.format(self.width,self.len))
































