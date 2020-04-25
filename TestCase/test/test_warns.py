#test_warns.py：对告警进行断言

import pytest
import make_warnings
import warnings

class TestWarns():

    #用pytest.warns()来断言告警，如果没有对应的告警抛出，则用例失败
    def test_warn(self):
        with pytest.warns(DeprecationWarning):
            make_warnings.make_warn()

    def test_no_warn(self):
        with pytest.warns(DeprecationWarning):
            make_warnings.not_warn()



#采用match正则匹配抛出的告警信息，若告警信息和告警类型不同时匹配，则用例执行失败
def warn_message1():
    warnings.warn("I'm a warning message", UserWarning)

def test_warn_match():
    with pytest.warns(UserWarning, match='^I.*e'):
        warn_message1()


#将告警信息存入一个变量中，通过读取这个变量中的信息进行断言，包括：告警的个数、告警信息参数等
def warn_message2():
    warnings.warn("user", UserWarning)
    warnings.warn("runtime", RuntimeWarning)

def test_warn_match_var():
    with pytest.warns(UserWarning, match = 'us') as record:
        warn_message2()

    assert len(record) == 2
    assert str(record[0].message) == "user"
    assert str(record[1].message) == "runtime"

#recwarn:一个用例级别的fixture，可以用来记录用例产生的所有告警
def test_catch(recwarn):
    warnings.warn("hello", UserWarning)
    assert len(recwarn) == 1
    w = recwarn.pop(UserWarning)
    assert issubclass(w.category, UserWarning)
    assert str(w.message) == "hello1"
    assert w.filename
    assert w.lineno
