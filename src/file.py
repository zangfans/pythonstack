#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：zangfans time:2019/6/20
import os
import time
from functools import reduce
import csv


# f = open('test1.txt','ab')
# f.write("\nhello world".encode('utf-8'))
# f.close()

# f1 = open('test.txt','rb')
# print(f1.read().decode())
# f1.close()

#上下文管理

# with open('test.txt','r') as read_f,open('test1.txt','w') as write_f:
#     data = read_f.read()
#     write_f.write(data)

#文件的修改
#读取另一个文件的内容，在存储到一个临时文件，删除原始文件，在移动临时文件到原文件名
# with open('test1.txt','r',encoding='utf-8') as read_f,open('test.txt.swap','w',encoding='utf-8') as write_f:
#     for line in read_f:
#         write_f.write(line)
# os.remove('test.txt')
# os.rename('test.txt.swap','test.txt')

# '''
# 文件内光标移动
# '''
# f = open("test.txt","r+")
# print('文件名为：',f.name)
#
# #读取每一行的数据并返回
# count = 1
# while count <= 2:
#     count += 1
#     line = f.readline()
#     print("读取到的数据: %s" %(line))
#
# f.seek(3,0)
# line = f.readline()
# print("读取到的数据: %s" %(line))
# f.close()


# st = open("st.txt","a")
# st.write("hello friend")
# st.close()



with open("st.txt","a+") as f:
    f.write("\nhi from python")

my_list = []
#读取文件对象并赋予列表中
with open("st.txt","r") as f:
    my_list.append(f.read())
print(my_list)


with open("st.csv","w") as f:
    w = csv.writer(f,delimiter=",")
    w.writerow(["one","two","three"])
    w.writerow(["four","five","six"])


















