from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="base.html"), name="home"),
    (r'^dictionary/', include('english.apps.dictionary.urls')),
    (r'^englishadmin/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns += patterns('',
            (r'^%s/(?P<path>.*)$' % settings.MEDIA_URL[1:-1],
                'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT}),
            (r'^404/$', 'django.views.defaults.page_not_found'),
            (r'^500/$', 'django.views.defaults.server_error'),
            (r'^admin/', include(admin.site.urls)),
    )
