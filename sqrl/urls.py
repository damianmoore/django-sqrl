from django.conf.urls import patterns, include, url


urlpatterns = patterns('sqrl.views',
    url(r'^qr-code/', 'qr_code', name='qr-code'),
    url(r'^auth/', 'sqrl_auth', name='sqrl-auth'),
)
