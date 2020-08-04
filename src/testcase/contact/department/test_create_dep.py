#ecoding=utf-8
# author:herui
# time:2019

from apis.contact.department.depmanagment import DepManagment
import pytest

class TestCreateDep:

    def test_create_new_dep(self):
        dept_managment = DepManagment()
        dept_managment.create_dept()
        create_res = dept_managment.get_response()
        assert create_res.get("errmsg") =="created"


    # 参数化的方法: @pytest.mark.parametrize("参数名"，["参数1"，"参数2"])
    @pytest.mark.parametrize("name",["测试1","测试2","测试3","测试5"])
    def test_create_new_dep_by_param(self,name):
        dept_managment = DepManagment()
        dept_managment.create_dept(name)
        create_res = dept_managment.get_response()
        assert create_res.get("errmsg") =="created"
