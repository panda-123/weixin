#ecoding=utf-8
# author:herui
# time:2019/11/19 17:41
# function:实现动态获取数据 和 断言配置化

from apis.contact.member.memberManagment2 import MemManagment
import chardet
import logging
import pytest
from utils import toolkits
from utils import randomchinese
from utils import comparator

class TestCreateMember:

    def test_create_member(self):
        member_Mangement = MemManagment()
        file_name = '../testdata/contact/member/member3.json'
        # file_name = r'E:\Hogwarts\python\weixin\testdata\contact\member\member3.json'
        json_object = member_Mangement.get_json_obj_from_file_with_reqres(file_name, "testcase1")
        old_value = json_object.get("userid")
        new_userid = toolkits.append_timeStamp_string(old_value)
        new_mobile = toolkits.get_random_mobile()
        email_prefix = toolkits.get_random_string()
        email_postfix = json_object.get("email").split('@')[1]
        logging.info("-----email后缀--:"+ email_postfix)
        new_email = email_prefix + "@" + email_postfix

        old_name = json_object.get("name")
        new_name = old_name + randomchinese.get_random_char(1)

        toolkits.update_json_value_by_key(json_object, "userid", new_userid)
        toolkits.update_json_value_by_key(json_object, "mobile", new_mobile)
        toolkits.update_json_value_by_key(json_object, "email", new_email)
        toolkits.update_json_value_by_key(json_object, "name", new_name)


        member_Mangement.create_member(json_object)
        create_res = member_Mangement.get_create_member_res()
        logging.info("-----新的userid--："+ json_object.get("userid"))
        # get from json file, convert to json_obj
        standar_result = member_Mangement.get_json_obj_from_file_with_reqres(file_name, "testcase1", "res")
        logging.debug("预期结果:" + str(standar_result))
        logging.debug("实际结果:" + str(create_res))
        json_comparator = comparator.JsonComparator()
        assert json_comparator.equal(create_res, standar_result)
