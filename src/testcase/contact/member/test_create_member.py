#ecoding=utf-8
# author:herui
# time:2019/11/19 17:41

from apis.contact.member.member import Member
from apis.contact.member.memberManagment import MemManagment
import chardet

import pytest

class TestCreateMember:
    # def test_create_member(self):
    #     memb = Member()
    #     memb.create_Member()
    #     create_res = memb.get_create_memb_res()
    #     assert create_res.get("errmsg") =="created"

    def test_create_new_member(self):
        member_Mangement = MemManagment()
        # file_name = r" E:\Hogwarts\python\weixin\testdata\contact\member\member.json"
        file_name = '../testdata/contact/member/member.json'
        member_Mangement.create_new_member(file_name)
        create_res = member_Mangement.get_create_new_member_res()
        assert create_res.get("errmsg") =="created"