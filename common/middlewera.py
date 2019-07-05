from django.utils.deprecation import MiddlewareMixin

from common import errors
from lib.http import render_json
from user.models import User


class AuthMiddleware(MiddlewareMixin):
    WHITE_LIST = [
        'api/verify_phone',
        'api/register'
    ]
    def process_request(self,request):
        if request.path in self.WHITE_LIST:
            return

        uid = request.session.get('uid')

        if uid is None:
            return render_json(code=errors.PHONE_NUM_ERR)

        request.user = User.objects.get(id=uid)

