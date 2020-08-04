#ecoding=utf-8
# author:herui
# time:2019

import logging
from apis.baseapi import BaseAPI
from initialization.sysconfig import sys_config
import requests
from utils import randomchinese
import time

class DepManagment(BaseAPI):

    def __init__(self):
        BaseAPI.__init__(self)
        logging.info("init department managment API")
        self.create_dept_url = sys_config.get('contact_para', 'create_dep_url')
        self.dep_secret = sys_config.get('contact_para', 'secret')
        self.update_dept_url = sys_config.get('contact_para', 'update_dep_url')
        self.del_dept_url = sys_config.get('contact_para', 'del_dep_url')
        self.get_depList_url = sys_config.get('contact_para', 'list_dep_url')

    def create_dept(self,name):
        # name = randomchinese.get_random_char(3) + time.strftime("%Y%m%d %S")
        new_part = {
            "name": name,
            "parentid": 1,
            "order": 1,
            # "id": 11
        }

        param = {"access_token":self.get_token(self.dep_secret)}
        logging.debug("url:"+str(self.create_dept_url))
        logging.debug("para:" + str(param))
        self.post_json(self.create_dept_url,new_part,params=param)

    def get_create_dept_res(self):
        return self.get_response()

    def update_dept(self):
        update_info = {
            "id": 5,
            "name": "和瑞20191114",
            "parentid": 1,
            "order": 1
        }
        param = {"access_token": self.get_token(self.dep_secret)}
        logging.info("url:" + str(self.create_dept_url))
        logging.info("para:" + str(param))
        self.post_json(self.update_dept_url, update_info, params=param)

    def get_update_dept_res(self):
        return self.get_response()

    def del_dept(self, del_id):
        param = {"access_token": self.get_token(self.dep_secret), "id": del_id}
        logging.debug("url:" + str(self.del_dept_url))
        logging.debug("para:" + str(param))
        del_res = requests.get(self.del_dept_url, params=param)
        return del_res.json()

    def get_dept_list(self, id1=0):
        param = {"access_token": self.get_token(self.dep_secret), "id": id1}
        logging.debug("url:" + str(self.get_depList_url))
        logging.debug("para:" + str(param))
        list_res = requests.get(self.get_depList_url, params=param)
        return list_res.json()

# if __name__ == '__main__':
#     dep_Mange = DepManagment()
#     print(dep_Mange.get_dept_list())

