from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526.StopInstanceRequest import StopInstanceRequest

client = AcsClient('<accessKeyId>', '<accessSecret>', 'cn-hangzhou')

request = StopInstanceRequest()
request.set_accept_format('json')

response = client.do_action_with_exception(request)
# python2:  print(response)
print(str(response, encoding='utf-8'))