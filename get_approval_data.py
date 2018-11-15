from wechat_work_api import *
from wechat_work_config import *
import time


def datetime2timestamp(datetime_str):
    """把datetime字符串，如：2018-11-13 15:10:20，转换为时间戳"""
    return int(time.mktime(time.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')))


start_time = datetime2timestamp('2018-11-13 15:15:00')
end_time = datetime2timestamp('2018-11-13 15:30:00')
next_sp_num = 201811130047

# 调用审批数据API
api = WechatWorkAPI(WECHAT_WORK_CONFIG['CORP_ID'], WECHAT_WORK_CONFIG['APPROVAL_APP_SECRET'])

try:
    response = api.http_call(WECHAT_WORK_API_TYPE['GET_APPROVAL_DATA'],
                             {'starttime': start_time, 'endtime': end_time, 'next_spnum': next_sp_num})
    print('错误返回码：', response['errcode'])
    print('错误信息：', response['errmsg'])
    print('拉取的审批单个数：', response['count'])
    print('时间段内的总审批单个数：', response['total'])
    print('拉取列表的最后一个审批单号：', response['next_spnum'])
    for apply_form in response['data']:
        print('审批单号:', apply_form['sp_num'])
        print('审批名称:', apply_form['spname'])
        print('审批状态:', apply_form['sp_status'])
        print('申请人姓名:', apply_form['apply_name'])
        print('申请人部门:', apply_form['apply_org'])
        print('审批人姓名:', apply_form['approval_name'])
        print('抄送人姓名:', apply_form['notify_name'])
        print('审批单提交时间:', apply_form['apply_time'])
        print('审批单提交者的userid:', apply_form['apply_user_id'])
        print('审批模板信息:', apply_form['comm'])
        # print('审批申请的单据数据:', apply_form['apply_data'])
        print('审批的附件media_id:', apply_form['mediaids'])
    print(response)

except WebServiceAPIException as err:
    print(err.err_code, err.err_msg)
