WECHAT_WORK_CONFIG = {

    # '通讯录同步'应用的secret, 在管理端->'管理工具'->'通讯录同步'里查询
    'CONTACT_SYNC_SECRET': 'E6udpT_U_p3nIIFsL8WY7haerb9EsNEReCue4HjnKmU',

    # 打卡应用的id及secrete，在管理端->'应用与小程序'->'打卡'->'API'里查询
    'CHECKIN_APP_ID': 3010011,
    'CHECKIN_APP_SECRET': 'UgyICn3973_Lr35d7wZ0yTDTxZztzu27meaveNnD0Vs',

    # 审批应用的id及secrete，在管理端->'应用与小程序'->'审批'->'API'里查询
    'APPROVAL_APP_ID': 3010040,
    'APPROVAL_APP_SECRET': 'zyFSVMi5gf21d5xDMG0bt0nOmRp45JdOlQsU51XTctU',

    # 自建应用'成本核算'的id及secret, 在管理端->'应用与小程序'->'成本核算'里查询
    'APP_ID': 1000018,
    'APP_SECRET': '7W-mwcGbbnmZE13P7JKhSX1hXY-16HBby52NNTOEvrw'}

if 'CORP_ID' not in WECHAT_WORK_CONFIG:
    WECHAT_WORK_CONFIG['CORP_ID'] = input('输入企业ID：')
