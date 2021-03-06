#-*- coding:utf-8 -*-
# author:peace
# datetime:2018/10/8 17:19
# file:test_process
# desc: 流程测试用例


import unittest
import requests
import os
import ddt
from util.baseApi import sendRequest,writeResult,writeResult2
from util.copyXls import copyXls
from util.readXlsUtil2 import readXlsUtil2
from util.loadConf import loadConf
from util import glb
from util.regFindString import regFindString
from util.replace import replace
from util.logUtil import Log
import manage

logger = Log("test_process")

# 当获取data目录
# dataPath = glb.dataPath
# reportPath = glb.reportPath
#
# dataXls = os.path.join(dataPath,loadConf.get_config('test','test_process','data_file'))
# reportXls = os.path.join(reportPath,loadConf.get_config('test','test_process','report_file'))

dataXls = manage.process_datafile
reportXls = manage.process_reportfile

# 读取测试数据
testData_pre = readXlsUtil2(dataXls).dict_data(0)
testData_norm = readXlsUtil2(dataXls).dict_data(1)
print('testData_norm:%s\n'%testData_norm)
print('testData_pre:%s\n'%testData_pre)


@ddt.ddt
class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.session = requests.session()
        copyXls(dataXls, reportXls)
        # 流程测试全都是普通用例，没有前置用例
        # for i in testData_pre:
        #     result = sendRequest(cls.session,i)
        #     writeResult(result,reportXls)

    @ddt.data(*testData_norm)
    def test_something(self,case_data):
        # 保存所有从响应中取出来的参数及值
        tmp ={}
        for data in case_data:
            print('data:%s\n'%data)
            if tmp == {}:
                logger.info("用例%s 没有关联参数" % data['caseId'])
            else:
                data['body'] = replace(data['body'], tmp).replace()
                data['params'] = replace(data['params'], tmp).replace()
                data['url'] = replace(data['url'], tmp).replace()
                data['headers'] = replace(data['headers'], tmp).replace()
            result = sendRequest(self.session,data)
            if data['re']:
                param = regFindString(result['text'],data['re']).find()
                for i in param:
                    tmp[i] = param[i]
            # writeResult(result,reportXls)
            writeResult2(result,reportXls)
        # self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
