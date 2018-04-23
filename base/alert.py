#-*-coding:utf-8 -*-
#author:huxiaodong
import urllib
import requests
import json
import urllib.parse
import urllib.request


class Alert:
    '''
    youzibuy alert api,(email|sms)
    '''
    # def __init__(self,email,phone,context):
    #     self.emal = email
    #     self.phone = phone
    #     self.context = context

    def sms(self):
        data = {}
        data["appkey"] = "b70929744c183a53"
        data["mobile"] = "18657176180"  # 手机号 超过1024请用POST
        data["content"] = "用户您好。【极速数据】"  # utf8

        url_values = urllib.parse.urlencode(data)
        url = "http://api.jisuapi.com/sms/send" + "?" + url_values
        request = urllib.request.Request(url)
        result = urllib.request.urlopen(request)
        jsonarr = json.loads(result.read())

        if jsonarr["status"] != u"0":
            print(jsonarr["msg"])
            exit()
        result = jsonarr["result"]

        print(result["count"], result["accountid"])


if __name__ == '__main__':
    a = Alert()
    a.sms()
