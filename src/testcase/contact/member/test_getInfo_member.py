#ecoding=utf-8
# author:herui
# time:2019/11/19 17:41

from apis.contact.member.member import Member
from apis.contact.member.memberManagment import MemManagment
import chardet
import pytest

class TestGetMember:
    # def test_create_member(self):
    #     memb = Member()
    #     memb.create_Member()
    #     create_res = memb.get_create_memb_res()
    #     assert create_res.get("errmsg") =="created"

    def test_get_info_member(self,userid):
        member_Mangement = MemManagment()
        get_res = member_Mangement.get_member_info(userid)
        assert get_res.get("errmsg") =="ok"

    @pytest.mark.parametrize("userid", ['littlecute', 'herui', 'huoyan'])
    def test_get_info_member_byParam(self,userid):
        member_Mangement = MemManagment()
        get_res = member_Mangement.get_member_info(userid)
        assert get_res.get("errmsg") =="ok"