#!/usr/bin/env python
#-*-coding:utf-8 -*-
import json
import math
import time
import random
from aliyunsdkcore.client import AcsClient
from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
from assets.models import Cloudprovider,Region
import re
# 'LTAIuSLn28HWNALb': 'O8Qobl7znrzcPIj90GAwu018OCrVkM'
# 'LTAIcSA5toFFbDGJ': 'FHWUSnWVA2ObJnpYDbmrG6bi5yuQQB'

__all__ = ['getinit']


def getinit(key,secret,region):
    client = AcsClient(
        "%s" % (key),
        "%s" %(secret),
        "%s" %(region)
    )

    request = DescribeInstancesRequest.DescribeInstancesRequest()
    request.set_PageSize(100)

    respone = client.do_action_with_exception(request)
    # print(respone)

    a = json.loads(respone)
    data = []
    for b in a.get('Instances')['Instance']:


        b['InnerIpAddress'] = b['InnerIpAddress']['IpAddress']

        EipAddress = []
        eipAddress = b['EipAddress']
        EipAddress.append(eipAddress)
        b['EipAddress'] = EipAddress

        VpcAttributes = []
        vpcAttributes = b['VpcAttributes']
        VpcAttributes.append(vpcAttributes)
        b['VpcAttributes'] = VpcAttributes


        b['SecurityGroupIds'] = b['SecurityGroupIds']['SecurityGroupId']


        b['PublicIpAddress'] =  b['PublicIpAddress']['IpAddress']

        OperationLocks = []
        operationLocks = ['OperationLocks']
        OperationLocks.append(operationLocks)
        b['OperationLocks'] = b['OperationLocks']['LockReason']

        data.append(b)
    return data

if __name__ == '__main__':
    a = getinit()
    print(a)