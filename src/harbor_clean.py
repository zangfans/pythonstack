#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：zangfans time:2019/6/21



'''
Harbor镜像清理

docker镜像仓库中镜像的清理，一直是个比较麻烦的事情。尤其是在测试环境当中，每天都会有大量的构建。由此会产生大量的历史镜像，而这些镜像，大多数都没有用。

在harbor中，清理镜像，也得分为两步，第一步是从ui中删除历史镜像。这个时候镜像并不会被真正删除，好在harbor集成了镜像删除的功能。

废话不多说，直接给操作。

###清理UI中的镜像
清理ui中的镜像，如果直接通过图形界面一个个的点击删除的话，在有大规模镜像需要清理的时候，简直就是灾难，而且这种方式，实在太low。

我这里简单写了个脚本，以实现如下功能：

遍历所有project
获取project中所有tag数超过30的repositories
获取这些tag数超过30的repositories的所有tag
基于时间排序，保留最新的30个tag
删除其他tag
脚本示例：
'''
import requests
import json


class RequestClient(object):

    def __init__(self, login_url, username, password):
        self.username = username
        self.password = password
        self.login_url = login_url
        self.session = requests.Session()
        self.login()

    def login(self):
        self.session.post(self.login_url, params={"principal": self.username, "password": self.password})


class ClearHarbor(object):

    def __init__(self, harbor_domain, password, schema="https",
                 username="admin"):
        self.schema = schema
        self.harbor_domain = harbor_domain
        self.harbor_url = self.schema + "://" + self.harbor_domain
        self.login_url = self.harbor_url + "/login"
        self.api_url = self.harbor_url + "/api"
        self.pro_url = self.api_url + "/projects"
        self.repos_url = self.api_url + "/repositories"
        self.username = username
        self.password = password
        self.client = RequestClient(self.login_url, self.username, self.password)

    def __fetch_pros_obj(self):
        # TODO
        self.pros_obj = self.client.session.get(self.pro_url).json()
        return self.pros_obj

    def fetch_pros_id(self):
        self.pros_id = []
        # TODO
        pro_res = self.__fetch_pros_obj()
        for i in pro_res:
            self.pros_id.append(i['project_id'])
        return self.pros_id

    def fetch_del_repos_name(self, pro_id):
        self.del_repos_name = []
        repos_res = self.client.session.get(self.repos_url, params={"project_id": pro_id})
        # TODO
        for repo in repos_res.json():
            if repo["tags_count"] > 30:
                self.del_repos_name.append(repo['name'])
        return self.del_repos_name

    def fetch_del_repos(self, repo_name):
        self.del_res = []
        tag_url = self.repos_url + "/" + repo_name + "/tags"
        # TODO
        tags = self.client.session.get(tag_url).json()
        tags_sort = sorted(tags, key=lambda a: a["created"])
        # print(tags_sort)
        del_tags = tags_sort[0:len(tags_sort) - 30]
        # print(del_tags)
        for tag in del_tags:
            del_repo_tag_url = tag_url + "/" + tag['name']
            print(del_repo_tag_url)
            del_res = self.client.session.delete(del_repo_tag_url)
            self.del_res.append(del_res)

        return self.del_res


if __name__ == "__main__":

    harbor_domain = "hub.test.com"
    password = "xxxxxxx"
    res = ClearHarbor(harbor_domain, password)
    # 循环所有的project id
    for i in res.fetch_pros_id():
        # 获取所有tag超过30的repos
        repos = res.fetch_del_repos_name(i)
        if repos:
            print(repos)
            for repo in repos:
                del_repos = res.fetch_del_repos(repo)
                print(del_repos)












































