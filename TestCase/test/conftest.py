import pytest

@pytest.fixture()
def some_data():
    print("begin")
    yield
    print("end")

@pytest.fixture()
def a_list():
    return [1,2,33,444,5555]


#fixture里面有个scope参数可以控制fixture的作用范围：session>module>class>function
#@pytest.fixture(scope="function"),没有指定时默认function

@pytest.fixture(scope = "class")
def scope_class():
    print("\nscope为class级别只运行一次")
    a = "yhm"
    return a


@pytest.fixture(scope = "module")
def scope_module():
    print("\nscope为module级别，当前.py模块只运行一次")
    a = "yhmm"
    return a


@pytest.fixture(scope = "session")
def scope_session():
    print("\nscope为session级别，可跨文件运行，多个.py模块只运行一次")
    a = "yhms"
    return a


par_to_test = [
    {
        "case":"search a word:python",
        "headers":{},
        "querystring":{
            "wd":"python"
        },
        "payload":{},
        "expected":{
            "status_code":200
        }
    },
    {
        "case":"search a word:java",
        "headers":{},
        "querystring":{
            "wd":"java"
        },
        "payload":{},
        "expected":{
            "status_code":200
        }
    },
    {
        "case":"search a word:go",
        "headers":{},
        "querystring":{
            "wd":"go"
        },
        "payload":{},
        "expected":{
            "status_code":200
        }
    }
]

@pytest.fixture(params = par_to_test)
def baidu_search(request):
    return request.param