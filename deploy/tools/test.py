#-*-coding:utf-8 -*-

import requests

url = 'http://511914614.ax.nofollow.51wtp.com/index.php/toupiao/h5/tsort?vid=511914614'

ret = requests.post(url)
print(ret.text)