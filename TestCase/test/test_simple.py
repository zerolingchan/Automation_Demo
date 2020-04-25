#test_simple.py

import requests

#测试文件以test_开头（以_test结尾也可以）
#测试类以Test开头，并且不能带有 init 方法
#测试函数以test_开头
#断言使用基本的assert即可

def test_one():
    r = requests.get('https://www.baidu.com')
    assert r.status_code == 200

def test_two():
    r = requests.get('https://www.baidu.com')
    assert r.encoding == 'utf'

#在多个文件添加测试用例使用fixture（scope_session)
def test_session(scope_session):
    print("测试账号：%s" % scope_session)
    assert scope_session == "yhms"