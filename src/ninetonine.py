#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：zangfans time:2019/12/19

for i in range(1,10):
    for j in range(1,10):
        result = i * j
        print("%d*%d=%-2d  " %(i, j, result), end="")
    print()



