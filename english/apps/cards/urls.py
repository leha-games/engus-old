from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from .views import CardViewSet


router = DefaultRouter(trailing_slash=False)
router.register(r'/cards', CardViewSet)


urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)
