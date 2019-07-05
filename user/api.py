from django.core.cache import cache
# from django.http import JsonResponse
# from django.shortcuts import render

# Create your views here.
from common import errors
from common import other_config
from common import utils
from lib.http import render_json
from user import logic
from user.forms import ProfileForm
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
    # #获取post请求的手机号
    # phone_num = request.POST.get('phone_num')
    # #验证手机号是否存在
    # if User.objects.filter(phone_num = phone_num):
    #     return render_json(code=errors.PHONE_NUM_EXIST_ERR)
    # #如果不存在，储存手机号
    # elif cache.get(phone_num) == request.POST.get('yzm'):
    #     User.objects.create(phone_num=phone_num)
    #     return render_json()
    # #存在则返回错误
    # else:
    #     return render_json(code=errors.YZM_NUM_ERR)

    phone_num = request.POST.get('phone_num', '')
    code = request.POST.get('code', '')

    phone_num = phone_num.strip()
    code = code.strip()

    # 1、检查 验证码
    cached_code = cache.get(other_config.VERIFY_CODE_CACHE_PREFIX % phone_num)
    if cached_code != code:
        return render_json(code=errors.VERIFY_CODE_ERR)

    # 2、登录或注册
    # try:
    #     user = User.objects.get(phonenum=phone)
    # except User.DoesNotExist:
    #     user = User.objects.create(phonenum=phone)
    user, created = User.objects.get_or_create(phone_num=phone_num)
    request.session['uid'] = user.id

    return render_json(data=user.to_dict())

def get_profile(request):
    profile = request.user.profile
    return render_json(data=profile.to_dict(exclude=['vibration', 'only_matche', 'auto_play']))

def set_profile(request):

    user = request.user

    form = ProfileForm(request.POST)

    if form.is_valid():
        profile = form.save(commit=False)
        profile.id = user.id
        profile.save()

        return render_json()
    else:
        return render_json(data=form.errors)


def upload_avatar(request):
    avatar = request.FILES.get('avatar')
    user = request.user

    # filename = 'avatar-%s-%d' % (user.id, int(time.time()))
    # filepath = os.path.join(settings.MEDIA_ROOT, filename)
    #
    # with open(filepath, 'wb+') as output:
    #     for chunk in avatar.chunks():
    #         output.write(chunk)

    ret = logic.async_upload_avatar(user, avatar)

    if ret:
        return render_json()
    else:
        return render_json(code=errors.AVATAR_UPLOAD_ERR)