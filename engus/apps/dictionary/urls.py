from django.conf.urls import patterns, url, include
from django.views.decorators.cache import cache_page
from rest_framework.routers import DefaultRouter
from .views import WordDetailView, FlatWordListView, ExampleViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'/examples', ExampleViewSet)

urlpatterns = patterns('',
    url(r'^/words/flat/$', cache_page(60 * 60 * 24 * 7)(FlatWordListView.as_view())),
    url(r'^/words/(?P<word>[^/]+)$', WordDetailView.as_view()),
    url(r'^', include(router.urls)),
)
