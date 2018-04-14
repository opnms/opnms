#-*- coding: utf-8 -*-

import sys
import hmac
import hashlib
import time
import requests
import json

AccessKey = 'kqlnim0khfpou45p'
SecretKey = '7226d410ef16427e821e61ebe30e8939'

params = 'accesskeykqlnim0khfpou45p'
timestamp = int(1000 * time.time())
print("timestamp: "+str(timestamp))
params = params + "timestamp" + str(timestamp)
print("params: "+params)
tempsign = SecretKey + params + SecretKey
print("sign: " + tempsign)

enc_res = hmac.new(SecretKey.encode(encoding="utf-8"), tempsign.encode(encoding="utf-8"), hashlib.md5).hexdigest()
print("hmacmd5: " + enc_res)

# url = 'http://open-ews.cloud.tmall.com/api/v1/service/?accesskey=kqlnim0khfpou45p&timestamp='
url = 'http://open-ews.cloud.tmall.com/api/v1/service/24059/?accesskey=kqlnim0khfpou45p&timestamp='
url = url + str(timestamp)
print("url: " + url)
headers = {"Authorization": enc_res.upper()}
print(headers)
r = requests.get(url, headers=headers)
#print r.text


data = json.loads(r.text)
print(data['data'])

for i in data['data']:
    print(i)
#print data['data']

# for i in data["data"]:
#     for ii in i["nodes"][0]["containers"]:
#         print(i["name"]+":"+str(ii["id"]))