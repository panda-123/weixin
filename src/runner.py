#ecoding=utf-8
# author:herui
# time:2019

import sys
import logging
from logging import handlers
import os
import pytest

sys.path.append(os.path.dirname(sys.modules[__name__].__file__))

# from initialization.sysconfig import sys_config

filename = 'E:/Hogwarts/python/weixin/log/auto.log'
# '../log/auto.log'

fileHandler = logging.FileHandler(filename=filename,encoding='utf-8')
logging.getLogger().setLevel(0)
# formatter = logging.Formatter('%(asctime)s - %(pathname)s - %(levelname)s: %(message)s')
formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
fileHandler.setFormatter(formatter)
logging.getLogger().addHandler(fileHandler)

if __name__ == '__main__':
    logging.info("-----------------start to excute automation cases------------------------------------")
    # 运行test_create_dep.py文件中的某一个方法，可用 '文件::类名::方法名' 来实现
    # pytest.main(['-sq', 'testcase/contact/department/test_create_dep.py::TestCreateDep::test_create_new_dep_by_param'])
    # pytest.main(['-sq', 'testcase/contact/member/test_create_member.py::TestCreateMember::test_create_new_member'])
    # pytest.main(['-sq', 'testcase/contact/member/test_create_member.py'])
    pytest.main(['-sq', 'testcase/contact/member/test_create_member5.py'])

    # pytest.main(['-sq', 'testcase/contact/department/test_del_dep.py'])
    # pytest.main(['-sq','testcase/contact/department/test_update_dep.py'])
    # pytest.main(['-sq', 'testcase/contact/department/test_getList_dep.py'])
    # pytest.main(['-sq', 'testcase/contact/member/test_getInfo_member.py::TestGetMember::test_get_info_member_byParam'])
    # pytest.main(['-sq', 'testcase/contact/member/test_update_member.py'])


