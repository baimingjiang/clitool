#coding=utf-8

import yaml
import os
import sys
import json
import io
import subprocess

def getConfig(full_key):
    key_list = full_key.split('.')

    self_dir = os.path.dirname(os.path.abspath(__file__))
    self_dir = os.path.split(self_dir)[0]
    
    cfg_file = os.path.join(self_dir, 'config.yaml')

    if os.path.exists(cfg_file):
        f = io.open(cfg_file, 'r', encoding = 'utf-8')
        f_data = f.read()
        f.close()
    else:
        rc_group_dir =  os.path.dirname(os.path.dirname(self_dir))
        cfg_file = os.path.join(rc_group_dir, 'config.yaml')
        if os.path.exists(cfg_file):
            f = io.open(cfg_file, 'r', encoding = 'utf-8')
            f_data = f.read()
            f.close()
        else:
            print(u"config.yaml 文件不存在，需要将 config.example.yaml 复制为 config.yaml 并进行配置")
            exit(1)

    conf = yaml.full_load(f_data)
    for key in key_list:
        conf = conf[key]
        
    return conf