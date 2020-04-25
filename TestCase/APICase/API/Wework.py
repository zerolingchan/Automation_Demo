import requests

#企业微信API测试
class Wework:
    token = ""

    #获取access_token,详情联系看企业微信API，corpid和corpsecret自行去企业微信获取
    @classmethod
    def get_token(cls):
        r = requests.get(
            url='https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            params={
                'corpid':'',
                'corpsecret':''
            }
        )

        cls.token = r.json()['access_token']
        return r