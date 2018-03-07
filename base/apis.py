import requests
import json
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "opnms.settings")
django.setup()
from rest_framework.authtoken.models import Token
from deploy.saltstack.saltapi import SaltstackAPI


class salthost_create_or_update:
    '''
    through api post and update data.
    '''

    def __init__(self, search,url):
        self.setup_header()
        self.search_params = search
        self.opnms_url = url

    def setup_header(self):
        self.opnms_header = {
            'Authorization': 'Token %s' % Token.objects.get(user=1),
            'Content-type': 'application/json',
            'Accept': 'application/json',
        }

    def get_data(self):
        id = ''
        data = requests.get(self.opnms_url, params=self.search_params, headers=self.opnms_header)
        if data.status_code == 200 and len(data.json()) > 0:
            id = data.json()[0]['id']
            return id
        else:
            return id

    def post_data(self, data):
        ret = requests.post(url=self.opnms_url, headers=self.opnms_header, data=json.dumps(data))
        print(ret.json())
        if ret.status_code == 200:

            return ret.json()
        else:
            return ret.status_code

    def put_data(self, id, data):
        ret = requests.put(url=self.opnms_url + str(id) + '/', headers=self.opnms_header, data=json.dumps(data))
        print(ret.json())
        if ret.status_code == 200:
            return True
        else:
            return False

    def main(self, data):
        code = self.get_data()
        if code:
            ret = self.put_data(code, data)
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
