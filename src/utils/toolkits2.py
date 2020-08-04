#ecoding=utf-8
# author:herui
# time:2019/11/27 17:57
# 方程老师写的工具集

import time
import random

def update_json_value_by_key(json_obj,key,new_value):
     json_obj[key]=new_value
     return json_obj

def append_time_stamp_string(old_value):
     return old_value+"_"+time.strftime('%Y%m%d%H%M%S')


def get_random_mobile():
    for k in range(10):
        prelist=["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
                 "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
                 "186", "187", "188", "189"]
        return random.choice(prelist)+"".join(random.choice("0123456789") for i in range(8))

def get_random_string(length=5):
     low_case = [chr(i) for i in range(65, 91)]
     up_cases =[chr(i) for i in range(97, 123)]
     all_string="".join(low_case)+"".join(up_cases) +"0123456789"
     return "".join(random.choice(all_string) for i in range(length))

if __name__=="__main__":
     print(get_random_string(6))