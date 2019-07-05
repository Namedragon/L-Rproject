"""
业务模块配置
"""
# 云之讯短信平台配置
YZX_SMS_URL = 'https://open.ucpaas.com/ol/sms/sendsms'

YZX_SMS_PARAMS = {
    'sid': 'e3876bed44f436923b28baf911a11713',
    'token': '9c8f54210318dc4b157d1a26352e2149',
    'appid': 'b86dd669ae0f46aab438d47d9d0d239b',
    'templateid': '482130',
    'param': None,
    'mobile': None
}

# 缓存 key prefix
VERIFY_CODE_CACHE_PREFIX = 'verfiy_code:%s'

# 七牛云配置
QN_ACCESS_KEY = 'ktgbAUqxq6D2WZ0PXRhRY4s5TvW2W_NcpuspuhcG'
QN_SECRET_KEY = 'XmsJZNH9LgCySF667ZtF-QZI1P6iI2tZXTwZw9ea'
QN_BUCKET = 'swiper'
QN_HOST = 'http://pu420clqe.bkt.clouddn.com'