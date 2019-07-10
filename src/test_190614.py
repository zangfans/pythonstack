#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：zangfans time:2019/6/14

# s1 = 'hello world'
# s = "hello world"
# s2="""hello world"""
# s3 = '"hello world"'

# print(str.split(s1))

# print(s.find('l'))
# print(s.index('lo'))
# print(s.find('a'))

# msg='name:{},age:{},gender:{}'
# print(msg.format("zangfan","24","male"))

# msg='name:{0},age:{1},gender:{0}'
# print(msg.format('aaaa','bbbb'))


# p1='name:{x},age:{y},gender:{z}'
# print(p1.format(x="zangfans",y="24",z="男"))

# while True:
#     name=input("name:")
#     age=input("age:")
#     gender=input("gender:")
#     height=input("height:")
#     msg='''
#             -------%s info---------
#             name:%s
#             age:%s
#             gender:%s
#             height:%s
#             ------------------------
#     '''%(name,name,age,gender,height)
#     print(msg)

# def re_sort():
#     s = input("请输入一串字符串: >>").strip()
#     return s[:]
# obj = re_sort()
# print(obj)

# while True:
#     name = input('user: ').strip()
#     password = input('password: ').strip()
#     if name == 'zangfan' and password == '1024':
#         print('login sucessfull')

'''
字符串分割split和拼接join
'''


# info='root:x:0:0:root:/root:/bin/bash'
# print(info[0]+info[1]+info[2]+info[3])
#
#
# user_l = info.split(':')
# print(user_l[:])
#
# detail_user = info.split(':')
# detail_shell = info.split(':')
# print('用户是: %s  命令是:%s' %(detail_user[0],detail_shell[6]))
#
# cmd='download|xhp.mov|3000'
# cmd_l=cmd.split('|')
# print(cmd_l[1])
# print(cmd_l[0])
# print(cmd.split('|',1))

# user_l1 = ['root', 'x', '0', '0', 'root', '/root', '/bin/bash']
# print(':'.join(user_l1))

# while True:
#     cmd = input('>>:  ').strip()
#     if len(cmd) == 0:continue
#     cmd_l=cmd.split()
#     print('命令是:%s 命令的参数是:%s' %(cmd_l[0],cmd_l[1]))

# print(len('hello world'))
# msg = 'hello world'
# print(msg[1:3])  #1 2
# print(msg[1:4])  #1 2 3

'''
判断个人年龄
'''
# zangfan_age = 24
# while True:
#     age = input('please input your age>>: ').strip()
#     if len(age) == 0:
#         continue
#     if age.isdigit():
#         age = int(age)
#         print('你的年龄是:%s' %(age))
#         break
#     else:
#         print('must be int')

#startswith,endswith
# name = 'zf_strange_sss'
# print(name.endswith('sss'))    #true
# print(name.startswith('zf'))       #true

#replace
# name='zangfan say :i have one tesla,my name is zangfan'
# print(name.replace('zangfan','god',1))

'''
字符串格式化
'''
# print('my name is %s my age is %s my gender is %s' %('zangfan',24,'male'))
# print('my name is {} my age is {} my gender is {}'.format('zangfan',24,'male'))
# print('my name is {0} my age is {1} my gender is {2}'.format('zangfan',24,'male'))
# print('my name is {name} my age is {age} my gender is {gender}'.format(name="zangfan",age=24,gender="male"))

#索引
# name = 'I have a dream'
# print(name.find('I',1,3))  #顾头不顾尾,找不到则返回-1,不会报错,找到了则显示索引
# print(name.index('I'))     #同上，但是找不到会报错
# print(name.count('a',1,8)) #顾头不顾尾，如果不指定范围则查找所有

'''
字母大小写转换
'''
# name = 'ZangFan'
# print(name.lower())
# print(name.upper())

#expandtabs
# name = 'zangfan\thello'
# print(name)
# print(name.expandtabs(1))


#captalize，swapcase，title

# print(name.capitalize())  #首写字母大写，其余部分小写
# print(name.swapcase())   #大小写翻转
# msg = "zangfan alex sunwukong"
# print(msg.title())    #每个单词的首字母大写

'''
判断数值类型:isdit,isdecimal,isnumeric,isalnum,isalpha,islower,isupper,isspace,istitile
'''

# num0='4'
# num1=b'4' #bytes
# num2=u'4' #unicode,python3中无需加u就是unicode
# num3='四' #中文数字
# num4='Ⅳ' #罗马数字

#isdigt：str,bytes,unicode
# print(num0.isdigit())    #Trure
# print(num1.isdigit())    #True
# print(num2.isdigit())    #True
# print(num3.isdigit())    #False
# print(num4.isdigit())    #False

#isdecimal：str,unicode
# print(num0.isdecimal())   #True
# print(num1)
# print(num2.isdecimal())   #True
# print(num3.isdecimal())   #False
# print(num4.isdecimal())   #False

#isnumeric:str,unicode,中文，罗马
# print(num0.isnumeric())     #True
# print(num2.isnumeric())     #True
# print(num3.isnumeric())     #True
# print(num4.isnumeric())     #True

# str1 = 'sjflsjl1233'
# str2 = 'sdfjslfj'
# print(str1.isalnum())    #字符串是否由字母和数字组成
# print(str2.isalpha())    #字符串是否由字母组成

# name = 'Zang Fan'
# print(name.islower())
# print(name.isupper())
# print(name.isspace())
# print(name.istitle())
# print(name.isidentifier())




























































