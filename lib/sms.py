from django.core.cache import cache


def send(phone_num,code):
    cache.set(phone_num,code,60)
    print('sms.send',phone_num,code)