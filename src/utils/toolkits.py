#ecoding=utf-8
# author:herui
# time:2019/11/27 17:57

import string
import random
import time

def update_json_value_by_key(json_obj, key, new_value):
    json_obj[key] = new_value
    return json_obj

def append_timeStamp_string(old_value):
    return old_value+ "_"+ time.strftime("%Y%m%d%H%M%S")


def get_random_mobile():
    for k in range(10):
        prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
                   "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
                   "186", "187", "188", "189"]
        return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))

def get_random_string(length=5):
    random_string = string.ascii_letters
    all_string = random_string+ "0123456789"
    return "".join(random.choice(all_string) for i in range(length))

# print(get_random_string(6))
