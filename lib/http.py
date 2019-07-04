from django.http import JsonResponse

from common import errors


def render_json(code=errors.OK,data=None):
    """
    自定义json输出
    :param code:
    :param date:
    :return:
    """

    result = {
        'code':code
    }

    if data:
        result["data"] = data

    return JsonResponse(result,json_dumps_params={'separators':(',',':')})