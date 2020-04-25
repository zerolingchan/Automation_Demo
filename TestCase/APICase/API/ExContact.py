import requests
from API.Wework import Wework

#企业微信外部联系人管理-客户管理模块，详细API看企业微信官网
class ExContact:

    #获取客户列表
    def list(self, uid):
        r = requests.get(
            url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/list',
            params={
                'access_token':Wework.token,
                'userid':uid
            }
        )
        return r


    #获取客户的详细信息
    def get(self, ex_uid):
        r = requests.get(
            url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get',
            params={
                'access_token':Wework.token,
                'external_userid':ex_uid
            }
        )
        return r

    #修改客户备注信息
    def remark(self, uid, ex_uid, remark):
        r = requests.post(
            url='https://qyapi.weixin.qq.com/cgi-bin/externalcontact/remark',
            params={
                'access_token':Wework.token
            },
            json={
                'userid':uid,
                'external_userid':ex_uid,
                'remark':remark
            }
        )
        return r