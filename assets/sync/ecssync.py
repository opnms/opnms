#!/usr/bin/env python
#-*-coding:utf-8 -*-
import requests
import json
from assets.sync.ecsToopnms import getinit
class AliyunToOpnms:
    opnms_url = 'http://127.0.0.1:8000/api/assets/v1/instance/'
    token = '0255242600a97c2a11faf619369c5db492f83ae2'

    def __init__(self,search):
        self.setup_header()
        self.search_params = search

    def setup_header(self):
        self.opnms_header = {
            'Authorization': 'Token %s' % self.token,
            'Content-type': 'application/json',
            'Accept': 'application/json',
        }

    def get_data(self):
        id = ''
        data = requests.get(self.opnms_url,params=self.search_params,headers=self.opnms_header)
        if data.status_code  == 200 and len(data.json()) > 0:
            id = data.json()[0]['id']
            return id
        else:
            return id

    def post_data(self,data):
        ret = requests.post(url=self.opnms_url,headers=self.opnms_header,data=json.dumps(data))
        print(ret.json())
        if ret.status_code == 200:

            return ret.json()
        else:
            return ret.status_code

    def put_data(self,id,data):
        ret = requests.put(url=self.opnms_url + str(id) + '/',headers=self.opnms_header,data=json.dumps(data))
        print(ret.json())
        if ret.status_code == 200:
            return True
        else:
            return False

    def main(self,data):
        code = self.get_data()
        if code:
            ret = self.put_data(code,data)
            if ret:
                print('Update ok')
            else:
                print('Update fail')
        else:
            ret = self.post_data(data)
            if ret:
                print('Post Ok')
            else:
                print('Post Fail')



if __name__ == '__main__':

    data = getinit()

    for instance in data:
        search = {
            'SerialNumber' : instance['SerialNumber'],
        }

        a = AliyunToOpnms(search)
        a.main(instance)
