from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = patterns('',
    url(r'^sqrl/', include('sqrl.urls')),
    url(r'^login/', 'sampleproject.views.login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='sampleproject/index.html')),
)
