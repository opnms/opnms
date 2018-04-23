#/usr/bin/env python
#-*- coding:utf-8 -*-
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

    token = '666b42aa52ed10e95e33e7abeee2faf37db6901e'
    def __init__(self,url):
        self.setup_header()
        #self.search_params = search
        self.setup_log()
        self.opnms_url = url
        #self.token = 'b9e48980e75003e8c9fa0eeeb360e9c1c839638b'
        self.salt_master = 'salt-master.internal.meetyima.com'
        self.salt_version = '2018.3.0-1.el7.noarch'

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
        console_handler.setLevel(logging.DEBUG)
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
        packages = ['dmidecode', 'lshw', 'ipmitool', 'OpenIPMI', 'm2crypto']
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
            'productname': '',
            'serialnumber': '',
            'osrelease': _distname + ' ' + _version
        }
        raw_ret = self.exec_cmd('/usr/sbin/dmidecode -t system')['stdout']
        for line in raw_ret.split('\n'):
            if line.startswith('\tManufacturer:'):
                ret['manufacturer'] = line.split(':')[1].replace('inc.', '').strip()
            elif line.startswith('\tProduct Name:'):
                ret['productname'] = line.split(':')[1].strip()
            elif line.startswith('\tSerial Number:'):
                serialnumber = line.split(':')[1].strip()
                if serialnumber == 'Not Specified':
                    serialnumber = ''
                ret['serialnumber'] = serialnumber
        self.log.info('Get system info success')
        return ret

    def setup_header(self):
        self.opnms_header = {
            'Authorization': 'Token {0}'.format(self.token),
            'Content-type': 'application/json',
            'Accept': 'application/json',
        }

    def _check_device_info(self, raw_info):
        """
        检查是否需要更新
        """
        ignore_update = True
        self.log.debug('checking device info......')
        #for each_item, each_value in self.device_info.iteritems():
        for each_item, each_value in self.device_info.items():
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
        self.log.debug('Searching device({0}) from opnms......'.format(self.device_info['serialnumber']))
        device_search_r = requests.get(self.opnms_url, params=search_params, headers=self.opnms_header)
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
                if device_info_r.status_code == 201:
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

    def device_initial(self,hostname):
        '''
        设置主机名
        :return:
        '''

        # 设置主机名
        self.log.debug('Setting hostname......')
        if gethostname() != hostname:
            self.log.debug('Raw hostname is {0}, Should set to {1}'.format(gethostname(), hostname))
            set_hostname = self.exec_cmd('sed -i "/^HOSTNAME=/d" /etc/hostname && '
                                    'echo "HOSTNAME={0}" >> /etc/hostname && '
                                    'hostname {0}'.format(hostname))
            if set_hostname['return_code'] != 0:
                self.log.warn('Set hostname failed, because: {0}'.format(set_hostname['stderr']))
                sys.exit(2)
            self.log.info('Set hostname success, new hostname: {0}'.format(gethostname()))
        else:
            self.log.info('Hostname is correct, ignore set')

        # 配置Salt Minion
        should_restart_salt_minion = False
        self.log.debug('Setting salt minion......')
        if self.exec_cmd('rpm -q salt-minion-{0}'.format(self.salt_version))['return_code'] != 0:
            # 安装Salt
            self.log.debug('Installing salt minion......')
            self.exec_cmd('systemctl stop salt-minion.service')
            self.exec_cmd('cd /opt/ && curl -L https://bootstrap.saltstack.com -o install_salt.sh')
            self.exec_cmd('cd /opt/ && sh install_salt.sh -P')
            self.log.info('Install salt minion success')
        else:
            self.log.info('Salt minion version is correct, ignore install/update')

        # 设置minion_id
        self.log.debug('Setting salt minion id')
        check_minion_id = self.exec_cmd('grep "{0}" /etc/salt/minion_id'.format(hostname))
        if check_minion_id['return_code'] != 0:
            set_minion_id = self.exec_cmd('echo "{0}" > /etc/salt/minion_id'.format(hostname))
            if set_minion_id['return_code'] != 0:
                self.log.warn('Set salt minion id failed, because: {0}'.format(set_minion_id['stderr']))
                sys.exit(2)
            should_restart_salt_minion = True
            self.log.info('Set salt minion id success')
        else:
            self.log.info('Salt minion id is correct, ignore set')

        # 设置master地址
        self.log.debug('Setting salt master address......')
        check_master_address = self.exec_cmd('egrep "^master: " /etc/salt/minion')
        if check_master_address['return_code'] != 0:
            set_master_address = self.exec_cmd('sed -i "/^#master: salt/a\master: {0}\" /etc/salt/minion'.format(
                self.salt_master))
            if set_master_address['return_code'] != 0:
                self.log.warn('Set salt master address failed, because: {0}'.format(
                    set_master_address['stderr']))
                sys.exit(2)
            should_restart_salt_minion = True
            self.log.info('Set salt master address success')
        else:
            self.log.info('Salt minion have set master address, ignore set')

        # 重启Salt minion并进行初始化

        if should_restart_salt_minion:
            self.log.debug('I will restart salt minion')
            restart_salt_minion = self.exec_cmd('systemctl enable salt-minion.service && systemctl restart salt-minion.service')
            if restart_salt_minion['return_code'] != 0:
                self.log.warn('Restart salt minion failed')
                sys.exit(2)
            self.log.info('Restart salt minion success')
            # sleep 5秒, 确保salt minion启动且key被master autosign
            time.sleep(5)

            # 同步模块

            self.log.debug('I will sync salt modules......')
            sync_salt_modules = self.exec_cmd('salt-call state.sls business.youzibuy')
            if sync_salt_modules['return_code'] != 0:
                self.log.warn('Sync salt modules failed, because: {0}'.format(sync_salt_modules['stdout']))
                self.log.info('Sync salt modules success')

            #修复requests
            self.exec_cmd('pip install requests urllib3 pyOpenSSL --force --upgrade')

    def start(self):
        self.device_info = {}
        self.device_info.update(self.system_info)
        self.device_info['create_by'] = 'beacon Agent'
        self.create_or_update()
        device_info = self.create_or_update()
        hostname = device_info.get('hostname')
        if hostname:
            self.device_initial(hostname)
        else:
            self.log.warn('Not found hostname, could not run device initial task')
            sys.exit(1)

if __name__ == '__main__':
    agent = BeaconAgent(
        url='http://120.27.205.29:80/api/assets/v1/server/'
    )
    agent.start()
