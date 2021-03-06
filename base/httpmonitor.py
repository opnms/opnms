#!/usr/bin/python
# coding: UTF-8
import pycurl
import sys
import os
class Test:
    def __init__(self):
        self.contents = ''
    def body_callback(self,buf):
        self.contents = self.contents + buf
def test_gzip(input_url):
    t = Test()
    #gzip_test = file("gzip_test.txt", 'w')
    c = pycurl.Curl()
    c.setopt(pycurl.WRITEFUNCTION,t.body_callback)
    c.setopt(pycurl.ENCODING, 'gzip')
    c.setopt(pycurl.URL,input_url)
    c.perform()
    http_code = c.getinfo(pycurl.HTTP_CODE)
    http_conn_time = c.getinfo(pycurl.CONNECT_TIME)
    http_pre_tran = c.getinfo(pycurl.PRETRANSFER_TIME)
    http_start_tran = c.getinfo(pycurl.STARTTRANSFER_TIME)
    http_total_time = c.getinfo(pycurl.TOTAL_TIME)
    http_size = c.getinfo(pycurl.SIZE_DOWNLOAD)
    print('http_code\nhttp_size\nconn_time\n pre_tran \nstart_tran\n total_time')
    print("%d \n%d \n%f\n %f\n %f\n %f"%(http_code,http_size,http_conn_time,http_pre_tran,http_start_tran,http_total_time))
if __name__ == '__main__':

    for url in open('test','r').readlines():
        print(url)
        input_url = url
        test_gzip(input_url)