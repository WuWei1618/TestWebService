from wechat_work_api import *
from wechat_work_config import *

# 调用企业微信通讯录API
api = WechatWorkAPI(WECHAT_WORK_CONFIG['CORP_ID'], WECHAT_WORK_CONFIG['CONTACT_SYNC_SECRET'])

try:
    response = api.http_call(WECHAT_WORK_API_TYPE['USER_GET'], {'userid': 'BaoZi'})
    print(response)

except WebServiceAPIException as err:
    print(err.err_code, err.err_msg)
