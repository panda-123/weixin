#ecoding=utf-8
# author:herui
# time:2019/11/19 17:41

from apis.contact.member.member import Member
from apis.contact.member.memberManagment import MemManagment
import chardet

import pytest
import logging

class TestUpdateMember:
    # def test_create_member(self):
    #     memb = Member()
    #     memb.create_Member()
    #     create_res = memb.get_create_memb_res()
    #     assert create_res.get("errmsg") =="created"

    def test_update_member(self):
        member_Mangement = MemManagment()
        # file_name = r" E:\Hogwarts\python\weixin\testdata\contact\member\member.json"
        file_name = r'E:\Hogwarts\python\weixin\testdata\contact\member\update_member.json'
        member_Mangement.update_member(file_name)
        update_res = member_Mangement.get_update_member_res()
        assert update_res.get("errmsg") == "updated"