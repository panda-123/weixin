#! /usr/bin/env python
#coding=utf-8
# 该部分已放至baseAPI中，目的：为了避免每次调用都运行一次

import requests

class GetAccessToken:
    access_token=''

    @staticmethod #静态变量，不需要初始化就可以使用
    def get_access_token():
        pass
        # requests.get()