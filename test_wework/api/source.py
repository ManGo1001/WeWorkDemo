import requests
from requests import post

from test_wework.api.baseapi import BaseApi
from test_wework.api.wework import WeWork


class Source(BaseApi):
    _tmp_url = "https://qyapi.weixin.qq.com/cgi-bin/media/upload"
    _long_url = "https://qyapi.weixin.qq.com/cgi-bin/media/uploadimg"

    def upload_tmp_source(self, type):
        tmp_content = { "Content-Type": "multipart/form-data",
                    "boundary":"-------------------------acebdf13572468",
                    "Content-Length":220,
                    "Content-Disposition":"form-data",
                    "name":"media",
                    "filename":"wework.txt",
                    "filelength":6,
                    "Content-Type": "application/octet-stream"
        }
        # self.request(post, self._tmp_url,
        #              params={"access_token": WeWork.get_app_token()},
        #              json=content, data=type)

        self.json_data = requests.post(self._tmp_url,
                                       params={"access_token": WeWork.get_app_token()},
                                       json=tmp_content).json()
        self.verbose(self.json_data)

    def upload_long_source(self):
        long_content = {
            "Content-Disposition":"form-data",
            "name":"fieldNameHere",
            "filename":"20180103195745.png",
            "Content-Type":"image/png",
            "Content-Length":220
            }
        self.json_data = requests.post(self._long_url, params={"access_token": WeWork.get_app_token()},
                                       json= long_content, data="file"
                                       ).json()
        self.verbose(self.json_data)
