import requests

from test_wework.api.baseapi import BaseApi


class WeWork(BaseApi):
    corpid = "ww28e8ded111eeb7f9"
    agentid = "1000002"
    agent_secret = "s_fKtbL48pYGSJGC4OLGjjRMZ4j-uqUZBRbkueV30oA"
    contact_secret = "psl_GtK8Nwm76y_wXwVWauaxkBPCuWvIjMge8-Tnjbs"
    address_secret = "hlSYe3rQv4flaysvO8T_HmgnT4-fIrgILJ7gQlScAn8"
    access_token_contact = None
    access_token_app = None
    access_token_addr = None

    @classmethod
    def get_access_token(cls):
        if cls.access_token_contact == None:
            url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
            r = requests.get(url, params={"corpid": cls.corpid, "corpsecret": cls.contact_secret}).json()
            print("first get token")
            cls.verbose(r)
            cls.access_token_contact = r["access_token"]
        return WeWork.access_token_contact

    @classmethod
    def get_app_token(cls):
        if cls.access_token_app == None:
            url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
            r = requests.get(url, params={"corpid": cls.corpid, "corpsecret": cls.agent_secret}).json()
            print("first get token")
            cls.verbose(r)
            cls.access_token_app = r["access_token"]
        return WeWork.access_token_app

    @classmethod
    def get_addr_token(cls):
        if cls.access_token_addr == None:
            url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
            r = requests.get(url, params={"corpid": cls.corpid, "corpsecret": cls.address_secret}).json()
            print("first get token")
            cls.verbose(r)
            cls.access_token_addr = r["access_token"]
        return WeWork.access_token_addr



