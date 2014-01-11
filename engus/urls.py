from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', 'engus.apps.accounts.views.home', name="home"),
    url(r'^accounts/password/done/$', 'django.contrib.auth.views.password_reset_done', { 'template_name': 'registration/password_reset_done.html' }, name='password_reset_done'),
    (r'^accounts/', include('registration.backends.default.urls')),
    (r'^cards', include('engus.apps.cards.urls')),
    (r'^dictionary', include('engus.apps.dictionary.urls')),
    (r'^engusadmin/', include(admin.site.urls)),
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
    urlpatterns += staticfiles_urlpatterns()
