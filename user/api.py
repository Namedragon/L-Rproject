from django.core.cache import cache
# from django.http import JsonResponse
# from django.shortcuts import render

# Create your views here.
from common import errors
from common import utils
from lib.http import render_json
from user import logic
from user.models import User


def verify_phone(request):
    #获取post请求的手机号
    phone_num = request.POST.get('phone_num')
    #验证手机号
    if utils.is_phone_num(phone_num.strip()):
        logic.send_verify_code(phone_num)
        return render_json()

    return render_json(code=errors.PHONE_NUM_ERR)

def register(request):
    #获取post请求的手机号
    phone_num = request.POST.get('phone_num')
    #验证手机号是否存在
    if User.objects.filter(phone_num = phone_num):
        return render_json(code=errors.PHONE_NUM_EXIST_ERR)
    #如果不存在，储存手机号
    elif cache.get(phone_num) == request.POST.get('yzm'):
        User.objects.create(phone_num=phone_num)
        return render_json()
    #存在则返回错误
    else:
        return render_json(code=errors.YZM_NUM_ERR)




