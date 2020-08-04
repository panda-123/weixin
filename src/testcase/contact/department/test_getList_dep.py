#ecoding=utf-8
# author:herui
# time:2019

from apis.contact.department.depmanagment import DepManagment
import pytest

class TestGetListDep:

    def test_get_deptList(self):
        dept_managment = DepManagment()
        del_res = dept_managment.get_dept_list()
        assert del_res.get("errmsg") == "ok"


    # # 参数化的方法: @pytest.mark.parametrize("参数名"，["参数1"，"参数2"])
    # @pytest.mark.parametrize("id", [19,20,21,22,23])
    # def test_del_dep_by_param(self, id):
    #     dept_managment = DepManagment()
    #     del_res = dept_managment.del_dept(id)
    #     assert del_res.get("errmsg") == "deleted"
