#ecoding=utf-8
# author:herui
# time:2019/11/19 17:41

from apis.contact.member.member import Member
from apis.contact.member.memberManagment2 import MemManagment
import chardet
import logging

import pytest

class TestCreateMember:

    def test_create_member(self):
        member_Mangement = MemManagment()
        file_name = '../testdata/contact/member/member2.json'
        json_object = member_Mangement.get_json_obj_from_file(file_name, "testcase1")
        member_Mangement.create_member(json_object.get("req"))
        create_res = member_Mangement.get_create_member_res()
        # get from json file, convert to json_obj
        standar_result = json_object.get("res")
        logging.debug("预期结果:" + str(standar_result))
        logging.debug("实际结果:" + str(create_res))
        assert create_res == standar_result