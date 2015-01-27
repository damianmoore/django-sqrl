from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from pysodium import *
import qrcode

from sqrl import base64url


def qr_code(request):
    uri = request.GET.get('sqrl-uri', '')
    img = qrcode.make(uri)
    response = HttpResponse(content_type='image/png')
    img.save(response, 'PNG')
    return response


@csrf_exempt
def sqrl_auth(request):
    nut = str(request.REQUEST.get('nut'))
    ids = str(request.REQUEST.get('ids'))
    server = base64url.decode(str(request.REQUEST.get('server')))
    client = base64url.decode(str(request.REQUEST.get('client')))
    client_dict = base64url.decode_dict(str(request.REQUEST.get('client')))
    import ipdb; ipdb.set_trace()
    crypto_sign_open(client, ids)
