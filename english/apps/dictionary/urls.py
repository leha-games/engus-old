from django.conf.urls import patterns, url
from django.views.decorators.cache import cache_page
from .views import WordDetailView, FlatWordListView


urlpatterns = patterns('',
    url(r'/words/flat/$', cache_page(60 * 15)(FlatWordListView.as_view())),
    url(r'/words/(?P<word>[^/]+)$', WordDetailView.as_view()),
)
