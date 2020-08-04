#ecoding=utf-8
# author:herui
# time:2019/11/19 16:41

from apis.baseapi import BaseAPI
import logging
from initialization.sysconfig import sys_config

class Member(BaseAPI):
    def __init__(self):
        BaseAPI.__init__(self)
        logging.info("init member API")
        self.create_member_url = sys_config.get('contact_para', 'create_member_url')
        self.dep_secret = sys_config.get('contact_para', 'secret')

    def create_Member(self):
        new_part = {
            "userid": "zhangsanyi",
            "name": "张三一",
            "alias": "jackzhang",
            "mobile": "15913215422",
            "department": [1, 3],
            "order":[],
            "position": "部门经理",
            "gender": "1",
            "email": "zhangsanyi@gzdev.com",
            "is_leader_in_dept": [1, 0],
            "enable":1,
            "avatar_mediaid": "",
            "telephone": "020-123456",
            "address": "广州市海珠区新港中路",
            "extattr": {},
            "to_invite": True,
            "external_position": "高级产品经理",
            "external_profile": {
                "external_corp_name": "",
                "external_attr": []
            }
        }

        param = {"access_token": self.get_token(self.dep_secret)}
        logging.debug("url:" + str(self.create_member_url))
        logging.debug("para:" + str(param))
        self.post_json(self.create_member_url, new_part, params=param)

    def get_create_memb_res(self):
        return self.get_response()

# if __name__ == '__main__':
#     logging.info("start")
#     out1 = Member()
#     out1.create_Member()
#     print(out1.get_create_memb_res())