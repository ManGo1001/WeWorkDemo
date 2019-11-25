import requests

from test_wework.api.baseapi import BaseApi
from test_wework.api.wework import WeWork


class Message(BaseApi):
    _send_url = "https://qyapi.weixin.qq.com/cgi-bin/message/send"

    def send_text(self, msg=None, users=[], parties=[], tags=[]):
        content = {
           "touser" : "|".join(users),
           "toparty" : "|".join(parties),
           "totag" : "|".join(tags),
           "msgtype" : "text",
           "agentid" : WeWork.agentid,
           "text" : {
               "content" : msg
           },
           "safe":0,
           "enable_id_trans": 0
        }
        self.json_data = requests.post(self._send_url,
                                       params= {"access_token": WeWork.get_app_token()},
                                       json= content,
                                       # proxies= self.proxies,
                                       verify= False).json()
        self.verbose(self.json_data)



    def send_voice(self):
        pass

    def send_video(self):
        pass
