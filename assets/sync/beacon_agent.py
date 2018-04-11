
import requests
import os
import sys
import time
import logging
import platform
import subprocess
import re
import json
from threading import Timer
import hashlib
from socket import gethostname


class BeaconAgent:


    def __init__(self,search,url,token):
        self.setup_header()
        self.search_params = search
        self.opnms_url = url
        self.token = token

    def exec_cmd(self,cmd, timeout=-1):
        _p = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        if timeout > 0:
            timer = Timer(timeout, _p.kill)
            timer.start()
            _stdout, _stderr = _p.communicate()
            if timer.is_alive:
                timer.cancel()
                ret = {
                    'return_code': _p.returncode,
                    'stdout': _stdout,
                    'stderr': _stderr
                }
            else:
                ret = {
                    'return_code': _p.returncode,
                    'stdout': '',
                    'stderr': 'process execute timeout'
                }
        else:
            _stdout, _stderr = _p.communicate()
            ret = {
                'return_code': _p.returncode,
                'stdout': _stdout,
                'stderr': _stderr
            }
        return ret

    def setup_log(self, log_file='/tmp/device_agent.log'):
        self.log = logging.getLogger('device_agent')
        self.log.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.WARN)
        formatter = logging.Formatter('%(asctime)s,%(msecs)03.0f [%(name)-17s][%(levelname)-8s] %(message)s')
        file_handler.setFormatter(formatter)
        self.log.addHandler(file_handler)
        self.log.addHandler(console_handler)

    def check_os(self):
        self.log.debug('Checking os ...')
        if platform.system().lower() != 'linux':
            self.log.warn('Only support Linux')
            sys.exit(2)

        _distname,_version,_ = platform.linux_distribution()
        if not(_distname.lower() in ['redhat','centos'] and _version.split('.')[0] == '7'):
            self.log.warn('Only support RHEL/Centos7')
            sys.exit(2)
        self.log.info('Checking Os Success.')

    def install_deps_packages(self):
        '''
        Install deps packages
        '''
        packages = ['python-requests', 'dmidecode', 'lshw', 'ipmitool', 'OpenIPMI', 'm2crypto']
        self.log.debug('Installing deps packages......')

        for each in packages:
            command = "rpm -q %s || yum -yq install %s" % (each, each)
            ret = self.exec_cmd(command)
            if ret['return_code'] != 0:
                self.log.warn('Package({0}) install failed, reason: {1}'.format(each, ret['stderr']))
                sys.exit(3)
        self.log.info('Install deps packages success')

    @property
    def system_info(self):
        self.log.debug('Getting system info.....')
        _distname, _version, _ = platform.linux_distribution()
        ret = {
            'manufacturer': '',
            'product_name': '',
            'serialnumber': '',
            'os': _distname + ' ' + _version
        }
        raw_ret = self.exec_cmd('/usr/sbin/dmidecode -t system')['stdout']
        for line in raw_ret.split('\n'):
            if line.startswith('\tManufacturer:'):
                ret['manufacturer'] = line.split(':')[1].replace('inc.', '').strip()
            elif line.startswith('\tProduct Name:'):
                ret['product_name'] = line.split(':')[1].strip()
            elif line.startswith('\tSerial Number:'):
                serialnumber = line.split(':')[1].strip()
                if serialnumber == 'Not Specified':
                    serialnumber = ''
                ret['serialnumber'] = serialnumber
        self.log.info('Get system info success')
        return ret

    def setup_header(self):
        self.opnms_header = {
            'Authorization': 'Token %s' % self.token,
            'Content-type': 'application/json',
            'Accept': 'application/json',
        }

    def _check_device_info(self, raw_info):
        """
        检查是否需要更新
        """
        ignore_update = True
        self.log.debug('checking device info......')
        for each_item, each_value in self.device_info.iteritems():
            if each_value != raw_info.get(each_item):
                ignore_update = False
                self.log.debug(
                    'found {0} different:\n\tlocal_info: {1}\n\toms_info: {2}'.format(
                        each_item,
                        each_value,
                        raw_info.get(each_item)))
                break
        return ignore_update

    def create_or_update(self):
        search_params = {'serialnumber':self.device_info['serialnumber']}
        self.log.debug('Searching device({0}) from oms......'.format(self.device_info['serialnumber']))
        device_search_r = requests.get(self.opnms_url, params=search_params, headers=self.token)
        if device_search_r.status_code == 200:
            device_info = device_search_r.json()
            # Create Device
            if not device_info:
                self.log.debug('Device not found, will create')
                self.log.debug('Device info: {0}'.format(json.dumps(self.device_info)))
                device_info_r = requests.post(
                    self.opnms_url,
                    data=json.dumps(self.device_info),
                    headers=self.opnms_header)
                if device_info_r.status_code == 200:
                    self.log.info('Device create success')
                else:
                    self.log.warn('Device create failed, status_code: {0}'.format(device_info_r.status_code))
                    sys.exit(1)
                device_info = device_info_r.json()
            else:
                # Check device info
                device_info = device_info[0]
                if not self._check_device_info(device_info):
                    self.log.debug('Device info different, updating......')
                    device_info_r = requests.put(
                        self.opnms_url + str(device_info['id']) + '/',  # Update URL
                        data=json.dumps(self.device_info),
                        headers=self.opnms_header)
                    if device_info_r.status_code == 200:
                        self.log.info('Device update success')
                        device_info = device_info_r.json()
                    else:
                        self.log.warn('Device update failed, status_code: {0}'.format(device_info_r.status_code))
                        sys.exit(1)
                else:
                    self.log.info('Device info same, ignore update')
            return device_info
        else:
            self.log.warn('Device search failed, status_code: {0}'.format(device_search_r.status_code))
            sys.exit(1)

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
        if ret.status_code == 200:

            return ret.json()
        else:
            return ret.status_code

    def put_data(self,id,data):
        ret = requests.put(url=self.opnms_url + str(id) + '/',headers=self.opnms_header,data=json.dumps(data))
        if ret.status_code == 200:
            return True
        else:
            return False

    def start(self):
        self.device_info = {}
        self.device_info.update(self.system_info)

if __name__ == '__main__':
    agent = BeaconAgent(
        opnms_url='http://127.0.0.1:8000/api/assets/v1/server/',
        token = '5632741b8367408ac21b54f31d00dcb1968c5aab'
    )
    agent.start()