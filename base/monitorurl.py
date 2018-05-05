#-*-coding:utf-8 -*-

import sys
import  hmac
import hashlib
import time
import requests
import json
import urllib
import top
import sys

class EwsService:
    '''
    Aliyun EWS service api
    '''
    def __init__(self,url):
        self.url = url
        self.context = self.get()

    def SetupHeaders(self):
        self.headers = {}

    def get(self):
        parames = {}
        print(self.url)
        req = requests.get(str(self.url))
        self.context = json.loads(req.text)
        return self.context

    def main(self):
        print(self.context)
        if self.context['code'] == 200 and len(self.context['data']) > 1:
            print(self.url + ':' + str(self.context['code']) + ' ' + 'is ok.')
        else:
            print(self.context)




if __name__ == '__main__':
    # a = EwsService(url='http://yzjcenter.hz.taeapp.com/tae_channel_brand?app_id=7&myuid=199983068&platform=android&v=2.4.8&channel_id=1')
    # a.main()
    for url in open('test','r').readlines():
        print(url)
        a = EwsService(url)
        a.main()