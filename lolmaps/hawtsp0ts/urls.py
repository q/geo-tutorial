from django.conf.urls.defaults import *

urlpatterns = patterns('lolmaps.hawtsp0ts.views',
    url(r'^$', 'index', name='lolmaps-index')
)
