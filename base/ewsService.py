#-*-coding:utf-8 -*-
import sys
import  hmac
import hashlib
import time
import requests
import json
import urllib
import top

class ewsServiceApi:
    '''
    Aliyun EWS service api
    '''

    def __init__(self,accesskey,secretkey):
        self.accesskey = accesskey
        self.secrekey = secretkey
        self.timestamp = int(1000 * time.time())


    def sign(self,secret, parameters):

        if hasattr(parameters, "items"):
            keys = parameters.keys()
            sorted(keys)
            parameters = "%s%s%s" % (secret,str().join('%s%s' % (key, parameters[key]) for key in keys),secret)
            # print(parameters)

        SecretKey = self.secrekey

        sign = hmac.new(
            SecretKey.encode('utf-8'),
            parameters.encode('utf-8'),
            hashlib.md5
        ).hexdigest().upper()
        return sign

    def get(self,geturl):

        parames = {
            'accesskey':self.accesskey,
            'timestamp':self.timestamp,
        }
        sign = self.sign(self.secrekey,parames)
        headers = {'Authorization':sign}
        req = requests.get(geturl,params=parames,headers=headers)
        context = json.loads(req.text)
        return context
        # print(context)



    def post(self, deployurl,node_id,comment):
        parameters = {
            'accesskey': self.accesskey,
            'comment':comment,
            'method': 'SEQUENTIAL',
            'node_id':node_id,
            'timestamp': self.timestamp,
            'update': "false",
            'url': deployurl,
        }

        sign = self.sign(self.secrekey,parameters)
        headers = {'Authorization':sign}
        serivceUrl = 'http://open-ews.cloud.tmall.com/api/v1/node/{0}/uploadStart/'.format(node_id)
        res = requests.post(url=serivceUrl,params=parameters,headers=headers)
        aa = json.loads(res.text)
        print(aa)


if __name__ == '__main__':
    a = ewsServiceApi(
        accesskey='kqlnim0khfpou45p',
        secretkey='7226d410ef16427e821e61ebe30e8939'
    )
    a.get(geturl='http://open-ews.cloud.tmall.com/api/v1/service/')
    a.post(deployurl = 'http://10.26.235.132/job/meetyou-youzijie-center-new/ws/youzijie-center.war',node_id=622290,comment='临时处理推荐商品专场过滤111')
