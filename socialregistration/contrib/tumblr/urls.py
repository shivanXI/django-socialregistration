from django.conf import settings
from socialregistration.compat.urls import *
from socialregistration.contrib.tumblr.views import TumblrRedirect, \
    TumblrCallback, TumblrSetup


urlpatterns = patterns('',
    url('^redirect/$', TumblrRedirect.as_view(), name='redirect'),
    url('^callback/$', TumblrCallback.as_view(), name='callback'),
    url('^setup/$', TumblrSetup.as_view(), name='setup'),
)
