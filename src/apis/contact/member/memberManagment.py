#ecoding=utf-8
# author:herui
# time:2019

import logging
import requests
from apis.baseapi import BaseAPI
from initialization.sysconfig import sys_config
from utils import randomchinese
import time
import codecs  # codecs用来处理中文编码的文件
import json

class MemManagment(BaseAPI):

    def __init__(self):
        BaseAPI.__init__(self)
        logging.info("init member managment API")
        self.create_member_url = sys_config.get('contact_para', 'create_member_url')
        self.dep_secret = sys_config.get('contact_para', 'secret')
        self.get_member_url = sys_config.get("contact_para", "get_member_url")
        self.update_member_url = sys_config.get("contact_para", "update_member_url")

    # 读取json文件，并转换为json对象（字典形式），返回json对象
    def get_new_member(self,file_name):
        with codecs.open(file_name, 'r', encoding='utf8') as f:
            # json.loads() 将str转为字典
            json_object = json.loads(f.read(), encoding='utf8')
            logging.debug('json_object'+str(json_object))
            return json_object

    def create_new_member(self,file_name):
        # name = randomchinese.get_random_char(3) + time.strftime("%Y%m%d %S")
        new_member = self.get_new_member(file_name)

        param = {"access_token":self.get_token(self.dep_secret)}
        logging.debug("url:"+str(self.create_member_url))
        logging.debug("para:" + str(param))
        self.post_json(self.create_member_url,new_member,params=param)

    def get_create_new_member_res(self):
        return self.get_response()

    def create_member(self,json_object):
        param = {"access_token":self.get_token(self.dep_secret)}
        logging.debug("url:"+str(self.create_member_url))
        logging.debug("para:" + str(param))
        self.post_json(self.create_member_url,json_object,params=param)

    def get_create_member_res(self):
        return self.get_response()

    def get_member_info(self, userid):

        param = {"access_token": self.get_token(self.dep_secret), "userid": userid}
        logging.debug("url:" + str(self.get_member_url))
        logging.debug("para:" + str(param))
        get_res = requests.get(self.get_member_url, params=param)
        logging.debug("信息:" + str(param["userid"]) + str(get_res.json()))
        return get_res.json()

    def update_member(self, file_name):
        update_info = self.get_new_member(file_name)
        param = {"access_token":self.get_token(self.dep_secret)}
        # logging.debug("url:" + str(self.update_member_url))
        # logging.debug("para:" + str(param))
        self.post_json(self.update_member_url, update_info, params=param)

    def get_update_member_res(self):
        return self.get_response()

# if __name__ == '__main__':
#     mem = MemManagment()
#     file_name = r'E:\Hogwarts\python\weixin\testdata\contact\member\update_member.json'
#     mem.update_member(file_name)
#     print(mem.get_update_member_res())