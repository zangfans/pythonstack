#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：zangfans time:2019/4/17
ids = [1,2,2,3,7,0,1001,1002,8,8,8,8]
news_ids = []
for id in ids:
    if id not in news_ids:
        news_ids.append(id)
print(news_ids)







