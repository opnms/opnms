from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException,ServerException
from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
from aliyunsdkecs.request.v20140526 import StopInstanceRequest
import json

client = AcsClient(
    'LTAIuSLn28HWNALb',
    'O8Qobl7znrzcPIj90GAwu018OCrVkM',
    'cn-hangzhou',
)

request = DescribeInstancesRequest.DescribeInstancesRequest()
request.set_PageSize(10)
respone = client.do_action_with_exception(request)
# print(respone)
print(json.loads(respone))