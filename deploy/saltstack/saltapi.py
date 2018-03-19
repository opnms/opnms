import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "opnms.settings")
django.setup()
import urllib
import urllib.parse
import urllib.request
import ssl,json
from deploy.models import SaltStack

__all__ = ['SaltstackAPI']

context = ssl._create_unverified_context()
ssl._create_default_https_context = ssl._create_unverified_context

class SaltstackAPI(object):
    def __init__(self):
        saltinfo = SaltStack.objects.all()
        self._url = [item.url for item in saltinfo][0].strip()
        self._user = [item.username for item in saltinfo][0].strip()
        self._password = [item.password for item in saltinfo][0].strip()


    def postRequest(self,params,prefix='/'):
        '''
        :param params:
        :param prefix:
        :return:
        '''
        url = self._url + prefix
        headers = {'X-Auth-Token': self.SaltToken()}
        req = urllib.request.Request(url,params, headers=headers)
        data = urllib.request.urlopen(req).read().decode("utf-8")
        content = json.loads(data)
        return content

    def SaltToken(self):

        params = {
            'eauth': 'pam',
            'username': self._user,
            'password': self._password
        }
        url = self._url + '/login'
        encode_params = urllib.parse.urlencode(params).encode(encoding='utf-8')
        req = urllib.request.Request(url,encode_params)
        content = json.loads(urllib.request.urlopen(req).read().decode("utf-8"))
        _token_id = content['return'][0]['token']
        return _token_id


    def list_all_key(self):
        '''
        获取包括认证、未认证salt主机
        '''

        params = {'client': 'wheel', 'fun': 'key.list_all'}
        obj = urllib.parse.urlencode(params).encode(encoding='utf-8')
        content = self.postRequest(obj)
        minions = content['return'][0]['data']['return']['minions']
        # minions_pre = content['return'][0]['data']['return']['minions_pre']
        return minions

    def Minions_status(self):
        '''
        获取minions 状态(up|down)
        :return:
        '''

        params = {'client':'runner','fun':'manage.status'}
        req = urllib.parse.urlencode(params).encode(encoding='utf-8')
        context =  self.postRequest(req)
        minions_up = context['return'][0]['up']
        minions_down = context['return'][0]['down']
        return minions_up,minions_down

    def Minion_grains(self,minion):
        '''
        获取minions grains 信息
        :param minion: minion == hostname
        :return:
        '''
        prefix = '/minions/' + minion
        url = self._url + prefix
        headers = {'X-Auth-Token': self._token_id}
        req = urllib.request.Request(url, headers=headers)
        data = urllib.request.urlopen(req).read().decode("utf-8")
        content = json.loads(data)
        ret = content['return'][0]['{0}'.format(minion)]
        print(ret)


    def remote_execution(self,tgt,fun,arg,tgt_type):
        '''
        异步执行远程命令、部署模块
        '''

        params = {'client': 'local_async', 'tgt': tgt, 'fun': fun, 'arg': arg, 'tgt_type': tgt_type}
        obj = urllib.parse.urlencode(params).encode(encoding='utf-8')
        content = self.postRequest(obj)
        jid = content['return'][0]['jid']
        print(jid)

    def remote_localexec(self,tgt,fun,arg,tgt_type):
        params = {'client': 'local', 'tgt': tgt, 'fun': fun, 'arg': arg, 'tgt_type': tgt_type}
        obj = urllib.parse.urlencode(params).encode(encoding='utf-8')
        content = self.postRequest(obj)
        ret = content['return'][0]
        print(ret)


if __name__ == '__main__':

    v = SaltstackAPI()

    v.SaltToken()
    # minon="hd-dev-biapp-01.youzibuy.com"
    # v.Minion_grains(minon)
    # v.list_all_key()
    up,down = v.Minions_status()
    print(up)
    print(down)
    host = '10.252.221.163,10.80.227.82'
    fun = 'cmd.run'
    arg = 'ls -l'
    tgt_type = 'list'
    v.remote_execution(tgt=host,fun=fun,arg=arg,tgt_type=tgt_type)




