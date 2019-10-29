#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：zangfans time:2019/10/24

#封装：
# 1.在面向对象编程中，对象将变量（状态）和方法（用来改变状态或执行涉及状态的计算）集中在一个地方--即对象本身。
# 2.隐藏的内部数据，以避免客户端代码（类外部的方法）直接进行访问。
#

#抽象
# 剥离事物的诸多特征，使其只保留最基本的特征

#多态
# 为不同的基础形态（数据类型）提供相关接口的能力。接口指的是函数或方法。

#继承
# 假设多个类存在相同的属性和行为时，我们同样可以将这些内容抽取到单独的一个类中，那么这些类就没有必要在定义这些属性和行为，只需要单独继承就可以了
# 子类改变从父类中继承方法的继承能力，被称为方法覆盖

#组合
# 通过组合技巧，将一个对象作为变量保存在另一个对象中，可以模拟拥有关系

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
    recs = []

    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.recs.append((self.width,self.len))

    def area(self):
        return self.width * self.len

    def change_size(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("""{} by {}""".format(self.width,self.len))
r1 = Rectangle(10, 10)
r2 = Rectangle(20, 20)
print(Rectangle.recs)

# rectangle = Rectangle(10, 20)
# print(rectangle.area())
# rectangle.change_size(20, 40)
# print(rectangle.area())


class shape():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print('''{} by {} '''.format(self.width,self.len))


class R1(shape):
    pass

obj2 = R1(10, 10)
print(obj2.print_size())


class Dog():
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person():
    def __init__(self, name):
        self.name = name

mick = Person("Mick jackson")
stan = Dog("Stanley", "Bulldog", mick)

print(stan.owner.name)






















