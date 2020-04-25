from API.Wework import Wework
from API.ExContact import ExContact
import requests
import pytest

class TestWework:

    @classmethod
    def setup_class(cls):
        cls.wework = Wework()
        cls.wework.get_token()
        cls.excontact = ExContact()

    #测试是否有获取到token
    def test_get_token(self):
        r = Wework.get_token()
        print(r.json())
        assert r.status_code == 200


    #参数化测试获取客户列表，参数自行填写
    @pytest.mark.parametrize("uid",[ ("" )])
    def test_list(self, uid):
        r = self.excontact.list(uid)
        print(r.json())
        assert r.status_code == 200
        assert len(r.json()['external_userid']) > 43


    #参数化测试获取客户详情，参数自行填写
    @pytest.mark.parametrize("uid",[ ("" )])
    def test_get(self, uid):
        r = self.excontact.list(uid)
        ex_uid = r.json()['external_userid'][0]
        r = self.excontact.get(ex_uid)
        print(r.json())
        assert r.status_code == 200


    #参数化测试修改客户备注信息，参数自行填写
    @pytest.mark.parametrize("uid, remark",[
        ("", ""),
        ("", ""),
        ("", "")
    ])
    def test_remark(self, uid, remark):
        r = self.excontact.list(uid)
        ex_uid = r.json()['external_userid'][0]
        self.excontact.remark(uid, ex_uid, remark)
        r = self.excontact.get(ex_uid)
        assert r.json()['follow_user'][0]['remark'] == remark
