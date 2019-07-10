#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：zangfans time:2019/6/19
import hashlib
import getpass
LIST_01 = []


def registers():
    print("请按提示创建用户信息")
    while True:
        print("(提示：输入用户名为 N/n时，退出输入)")
        name = input("输入用户名: ")
        if name.upper() == "N":
            break
        pwd = getpass.getpass("密码")
        password = get_md5(pwd)
        temp = {"user_name": name, "password": password}
        LIST_01.append(temp)


def get_md5(data):
    obj = hashlib.md5("wenxing".encode("utf-8"))
    obj.update(data.encode("utf-8"))
    password = obj.hexdigest()
    return password


def login():
    print("**********登录************")
    user = input("用户名")
    pwd = getpass.getpass("密码")

    for item in LIST_01:
        if item["user_name"] == user and item["password"] == get_md5(pwd):
            return True


registers()
print(LIST_01)
result = login()
if result:
    print("成功")
else:
    print("失败")