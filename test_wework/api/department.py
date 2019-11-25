import requests

from test_wework.api.baseapi import BaseApi
from test_wework.api.wework import WeWork


class Department(BaseApi):
    list_url = "https://qyapi.weixin.qq.com/cgi-bin/department/list"
    create_url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
    delete_url = "https://qyapi.weixin.qq.com/cgi-bin/department/delete"
    update_url = "https://qyapi.weixin.qq.com/cgi-bin/department/update"

    def list(self, id):
        self.json_data = requests.get(self.list_url, params={"access_token": WeWork.get_access_token(), "id": id}).json()
        self.verbose(self.json_data)
        return self.json_data

    def create(self, name, parentid, order, id):
        proxy_addr = {
            'http': 'http://127.0.0.1:7788',
            'https': 'https://127.0.0.1:7788'
        }
        data = {"name": name, "parentid": parentid, "order": order, "id": id}
        self.json_data = requests.post(self.create_url,
                          params={"access_token": WeWork.get_addr_token()},
                          #设置一个UTF8编码
                          headers={'content-type':'application/json; charset=utf-8'},
                          json=data,
                          #proxies=proxy_addr,
                          verify=False
                          ).json()
        self.verbose(self.json_data)
        return self.json_data


    def delete(self, id):
        self.json_data = requests.get(self.delete_url, params={"access_token": WeWork.get_addr_token(), "id": id}).json()
        self.verbose(self.json_data)
        return self.json_data


    def update(self, id, name, parentid, order):
        data = {"id": id, "name": name, "parentid": parentid, "order": order}
        self.json_data = requests.post(self.update_url, json= data,
                                    params= {"access_token": WeWork.get_addr_token()}).json()
        self.verbose(self.json_data)
        return self.json_data


