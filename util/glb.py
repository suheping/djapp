#-*- coding:utf-8 -*-
# author:peace
# datetime:2018/10/12 21:49
# file:glb.py
# desc: 定义全局变量
import os,time
import manage

# reportPath_base = os.path.abspath(os.path.join(os.getcwd(),'../report'))
reportPath_base = manage.reprot_dir
# 判断是否有report目录，没有就创建
if not os.path.exists(reportPath_base):
    os.mkdir(reportPath_base)

ctime = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
reportPath = os.path.join(reportPath_base,ctime)
# 判断report下边是否有时间戳文件夹，没有就新建
if not os.path.exists(reportPath):
    os.mkdir(reportPath)

# dataPath = os.path.abspath(os.path.join(os.getcwd(),'../data'))
dataPath = manage.data_dir
casePath = manage.case_dir