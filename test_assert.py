#test_assert.py：断言练习

#对于模块和自己写的脚本不在同一个目录下，在脚本开头加sys.path.append('xxx')
#import sys
#sys.path.append(".")


import requests
import pytest
import is_leap_year


class TestAssert():

    #断言预期的异常：在测试过程中，对某些方法进行测试时，预测输入某些特定数据，会抛出特定异常，若出现特定异常，则用例执行通过
    def test_assert(self):
        r = requests.get('https://www.baidu.com')
        assert r.status_code == 100,"返回200说明访问成功"
    

    #判断is_leap_year函数是闰年的测试函数
    def test_true(self):
        assert is_leap_year.is_leap_year(400) == True
    

    #直接用pytest.raises()处理异常，不用断言
    def test_exception_typeerror(self):
        with pytest.raises(TypeError):
            is_leap_year.is_leap_year('aa')


    #将异常信息存储在变量中，再读取异常信息进行断言判断
    def test_exception_value(self):
        with pytest.raises(ValueError) as excinfo:
            is_leap_year.is_leap_year(0)

        assert "从公元1年开始" in str(excinfo.value)
        assert excinfo.type == ValueError


    #对异常输出信息进行断言，异常类型、异常输出信息同时匹配成功，用例才可以执行成功
    #如下的例子，将Pattern的内容改为可以匹配的信息，则用例执行成功
    def test_exception_match(self):
        with pytest.raises(ValueError, match='公元145年是从公元1年开始的') as excinfo:
            is_leap_year.is_leap_year(0)

        assert excinfo.type == ValueError

    #标记预计失败的函数：pytest.mark.xfail(raises = xx)
    @pytest.mark.xfail(raises = ValueError)
    def test_mark(self):
        is_leap_year.is_leap_year(-100)