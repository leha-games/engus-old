from django.conf.urls import patterns, url
from django.views.decorators.cache import cache_page
from .views import WordDetailView, FlatWordListView


urlpatterns = patterns('',
    url(r'(?P<word>[^/]+)$', WordDetailView.as_view()),
    url(r'$', cache_page(60 * 15)(FlatWordListView.as_view())),
)
