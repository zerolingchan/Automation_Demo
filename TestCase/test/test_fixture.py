import pytest
import requests

#fixture是在测试函数运行前后，由pytest执行的外壳函数
#包括定义传入测试中的数据集，配置测试前系统的初始状态，为批量测试提示始建于等
#fixture是pytest用于将测试前后进行预备，清理工作的代码分离出核心测试逻辑的一种机制

#@pytest.fixture()装饰器声明函数为一个fixture


#测试函数的参数列表包含fixture名字，pytest可以检测到
#检测顺序：优先搜索该测试所在的模块，然后搜索conftest.py，并在测试函数运行之前执行该fixture
#fixture可以完成测试任务，也可以返回数据给测试函数
def test_some_data(some_data):
    print("test")

#使用pytest --setup-show 文件名 可以看到执行顺序
#fixture函数可以放在单独的测试文件里
#如果希望多个测试文件共享fixture，可以放在某个公共目录下新建一个conftest文件，将fixture放在里面

def test_a_list(a_list):
    assert a_list[2] == 33


class TestScope_class():
    def test_1(self, scope_class):
        print("测试账号：%s" % scope_class)
        assert scope_class == "yhm"

    def test_2(self, scope_class):
        print("测试账号：%s" % scope_class)
        assert scope_class == "yhm"


def test_module(scope_module):
    print("测试账号：%s" % scope_module)
    assert scope_module == "yhmm"

class TestScope_module():
    def test_1(self, scope_module):
        print("测试账号：%s" % scope_module)
        assert scope_module == "yhmm"

    def test_2(self, scope_module):
        print("测试账号：%s" % scope_module)
        assert scope_module == "yhmm"


def test_session(scope_session):
    print("测试账号：%s" % scope_session)
    assert scope_session == "yhms"


def test_baidu_search(baidu_search):
    url = "https://www.baidu.com"
    r = requests.request("GET", url, data = baidu_search["payload"], headers = baidu_search["headers"], params = baidu_search["querystring"])
    assert r.status_code == baidu_search["expected"]["status_code"]