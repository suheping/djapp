#-*- coding:utf-8 -*-
# author:peace
# datetime:2018/10/12 9:36
# file:loadConf
# desc: 读取配置文件

import configparser
import os
import manage




class LoadConfNew(configparser.ConfigParser):
    def as_dict(self):
        """
        将configparser.ConfigParser.read()读取到的数据转换成dict类型返回
        :return:
        """
        d = dict(self._sections)
        for k in d:
            d[k] = dict(d[k])
        return d

if __name__ == '__main__':
    # x = loadConf.get_config('test','test_api','report_file')
    # print('x:'+x)
    # y = loadConf.get_config('test','test_process','data_file')
    # print('y：'+ y)
    # path = os.path.join(confPath,x)
    # print(path)
    cfg = LoadConfNew()
    cfg.read("E:\\pyworkspace\\djapp\\conf\\test\\config.conf",encoding='utf8')
    print(cfg.as_dict())
