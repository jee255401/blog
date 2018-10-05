from django.conf.urls import url
from . import views  # views.~ 형식으로 변경해야 함
urlpatterns = [
    url(r'^bookmark/$', views.BookmarkLV.as_view(), name='index'),
    url(r'^bookmark/(?P<pk>\d+)/$', views.BookmarkDV.as_view(), name='detail'),
    url(r'^bookmark_t_CBV/$', views.BookmarkLV.as_view(), name='index_t_CBV'),
    url(r'^bookmark_t_FBV/$', views.tabularBookmark, name='index_t_FBV'),
]