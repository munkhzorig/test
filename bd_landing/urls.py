from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bd_landing.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    (r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^$', 'join.views.main', name='main'),
    url(r'^norm/$', 'join.views.norm', name='norm'),
    url(r'^features/$', 'join.views.features', name='features'),
    url(r'^admin/', include(admin.site.urls)),
)
