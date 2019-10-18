#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：zangfans time:2019/10/12

# import sys
# for i in sys.modules:
#     print(i)
#     print(i)



import sys
def sqlparse():
    print('from mysql sqlparse')

def sqlpare():
    print('from oracle sqlparse')

db_type = input('>>: ')
if db_type == 'mysql':
    import mysql as db
elif db_type == 'oracle':
    import oracle as db
db.sqlparse()



