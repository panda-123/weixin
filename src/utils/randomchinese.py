#ecoding=utf-8
# author:herui
# time:2019-11-14

import random

def get_random_char(number):
    val_list = [ ]
    for n in range(0, number):
        # 简体中文编码范围：4E00-9FA5
        val_list.append(chr(random.randint(0x4E00, 0x9FA5)))
    return "".join(val_list)

# print(get_random_char(2))




