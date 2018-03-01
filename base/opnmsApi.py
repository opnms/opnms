#!/usr/bin/env python
#-*-coding:utf-8 -*-
import requests


class AliyunToOpnms:
    opnms_url = 'http://127.0.0.1:8000/api/assets/v1/instance/'
    token = '52fce535e36db5ce1eb2ce214d340dd1e954e631'

    def __init__(self):
        self.setup_header()

    def setup_header(self):
        self.opnms_header = {
            'Authorization': 'Token %s' % self.token,
            'Content-type': 'application/json',
            'Accept': 'application/json',
        }

    def get_data(self):
        search_params = {}
        data = requests.get(self.opnms_url,params=search_params,headers=self.opnms_header)
        if data.status_code  == 200:
            return data
        else:
            raise ValueError(data)

    def post_data(self):
        data = self.get_data()
        ret = requests.post(url=self.opnms_url,headers=self.opnms_header,data=data)
        if ret.status_code == 200:
            return True
        else:
            print(ret.status_code)

if __name__ == '__main__':
    a = AliyunToOpnms()
    a.post_data()