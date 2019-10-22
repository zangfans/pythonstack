#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：zangfans time:2019/10/12

import math
import random
import statistics
import keyword


# import sys
# for i in sys.modules:
#     print(i)
#     print(i)

#将大型程序分割成多个包含Python代码的文件，也被成为模块.模块中支持使用另一个模块的代码。Python解释器自带内置模块

# import sys
# def sqlparse():
#     print('from mysql sqlparse')
#
# def sqlpare():
#     print('from oracle sqlparse')
#
# db_type = input('>>: ')
# if db_type == 'mysql':
#     import mysql as db
# elif db_type == 'oracle':
#     import oracle as db
# db.sqlparse()


print(math.pow(2,3))
print(random.randint(0,100))

nums = [1, 5, 33, 12, 46, 33, 2]
#均值
print(statistics.mean(nums))
#中值
print(statistics.median(nums))
#众数
print(statistics.mode(nums))


print(keyword.iskeyword("for"))
print(keyword.iskeyword("zangfans"))





