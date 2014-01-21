from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'profiles', ProfileViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^', include('registration.backends.default.urls')),
    url(r'^accounts/password/done/$', 'django.contrib.auth.views.password_reset_done', { 'template_name': 'registration/password_reset_done.html' }, name='password_reset_done'),
)
