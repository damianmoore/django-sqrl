from django.shortcuts import render_to_response
from django.utils.crypto import get_random_string
from pysodium import randombytes

from sqrl import base64url


def login(request):
    host = request.META['HTTP_HOST']
    nut = base64url.encode(randombytes(32))
    context = {}
    context['sqrl_uri'] = 'qrl://{}/sqrl/auth/?nut={}'.format(host, nut)
    return render_to_response('sampleproject/login.html', context)
