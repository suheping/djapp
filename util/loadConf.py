#-*- coding:utf-8 -*-
# author:peace
# datetime:2018/10/12 9:36
# file:loadConf
# desc: 读取配置文件

import configparser
import os
import manage




class loadConf():

    @classmethod
    def get_config(cls,username,section,option):
        # 配置文件路径
        # confPath = os.path.abspath(os.path.join(os.getcwd(), "../conf"))
        confPath = manage.conf_dir
        print('os.getcwd:' + os.getcwd())

        confFile = os.path.join(confPath, username + '\config.conf')
        print('配置文件为：' + confFile)
        cf = configparser.ConfigParser()
        cf.read(confFile, encoding='utf8')

        value = ''
        try:
            value = cf.get(section,option)
            print(value)
        except:
            print('section、option填写有误，请检查')
        finally:
            return value


if __name__ == '__main__':
    x = loadConf.get_config('test','test_api','report_file')
    print('x:'+x)
    y = loadConf.get_config('test','test_process','data_file')
    print('y：'+ y)
    # path = os.path.join(confPath,x)
    # print(path)
