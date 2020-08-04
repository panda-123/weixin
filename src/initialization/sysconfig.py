#ecoding=utf-8
# author:herui
# time:2019
# function：读取配置文件auto.cfg内容

import configparser
import logging
import os

def read_config(cfg_file):
    cfg = configparser.ConfigParser()
    # print("current dir:" + os.getcwd()) #获取当前路径
    if os.path.isfile(cfg_file):
        cfg.read(cfg_file)
        return cfg
    else:
        logging.warning(cfg_file + ' --file is not exist!!!')


file_path = r"E:\Hogwarts\python\weixin\cfg\auto.cfg"
# 用相对路径报错，待确认解决： AttributeError: 'NoneType' object has no attribute 'get'
# file_path = "../../cfg/auto.cfg"
sys_config = read_config(file_path)

if __name__ == "__main__":
    cfg = read_config(file_path)
    print(cfg.get('contact_para', 'create_dep_url'))