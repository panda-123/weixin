#ecoding=utf-8
# author:herui
# time:2019
# function：读取JSON文件，创建成员

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


    def get_json_obj_from_file_with_reqres(self, file_name, testcase_name, type='req'):
        with codecs.open(file_name, 'r', encoding='utf8') as f:
            # json.loads() 将str转为字典
            multiple_json_object = json.loads(f.read(), encoding='utf8')
            case_json_object = multiple_json_object.get(testcase_name).get(type)
            # logging.debug('json_object'+str(case_json_object))
            return case_json_object

    def create_member(self, json_object):
        param = {"access_token":self.get_token(self.dep_secret)}
        # logging.debug("url:"+str(self.create_member_url))
        # logging.debug("para:" + str(param))
        self.post_json(self.create_member_url,json_object,params=param)

    def get_create_member_res(self):
        return self.get_response()


if __name__ == '__main__':
    mem = MemManagment()
    file_name = r'E:\Hogwarts\python\weixin\testdata\contact\member\member2.json'
    json_obj = mem.get_json_obj_from_file_with_reqres(file_name, "testcase2")
    mem.create_member(json_obj)
    print(mem.get_create_member_res())