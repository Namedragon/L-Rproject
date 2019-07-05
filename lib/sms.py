from django.conf import settings
import requests
from django.core.cache import cache

from common import other_config


# def send(phone_num,code):
#     cache.set(other_config.VERIFY_CODE_CACHE_PREFIX % phone_num,60)
#     print('sms.send',phone_num,code)
def send(phone_num, code):
    if settings.DEBUG:
        print(phone_num, code)
        return True

    params = other_config.YZX_SMS_PARAMS.copy()
    params['mobile'] = phone_num
    params['param'] = code

    resp = requests.post(other_config.YZX_SMS_URL, json=params)

    if resp.status_code == 200:
        result = resp.json()
        if result.get('code') == '000000':
            return True
    return False