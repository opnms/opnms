#-*-coding:utf-8 -*-

import sys
import  hmac
import hashlib
import time
import requests
import json
import urllib
import top

class EwsService:
    '''
    Aliyun EWS service api
    '''

    def __init__(self,accesskey,secretkey):
        self.accesskey = accesskey
        self.secrekey = secretkey
        self.tempstamp = int(1000 * time.time())
        self.SetupHeaders()

    def SingKey(self):
        tempaccesskey = 'accesskey' + self.accesskey
        pamas = tempaccesskey + 'timestamp' + str(self.tempstamp)
        tempsign = self.secrekey + pamas + self.secrekey
        SecretKey = self.secrekey
        signkey = hmac.new(
            SecretKey.encode(encoding='utf-8'),
            tempsign.encode(encoding='utf-8'),
            hashlib.md5).hexdigest()
        return signkey


    def SetupHeaders(self):
        self.headers = {
            'Authorization': self.SingKey().upper()
        }

    def get(self,geturl):

        parames = {
            'accesskey':self.accesskey,
            'timestamp':self.tempstamp,
        }
        httpurl = geturl

        req = requests.get(httpurl,params=parames,headers=self.headers)
        context = json.loads(req.text)
        return context
        # print(context)



if __name__ == '__main__':
    a = EwsService(
        accesskey='kqlnim0khfpou45p',
        secretkey='7226d410ef16427e821e61ebe30e8939',
        # url='http://open-ews.cloud.tmall.com/api/v1/service/'
    )
    a.get(geturl='http://open-ews.cloud.tmall.com/api/v1/service/')