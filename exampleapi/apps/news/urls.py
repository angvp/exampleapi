from django.conf.urls import url

from news.views import PostList, PostDetail

urlpatterns = [
    url(r'^$', PostList.as_view(), name='post-list'),
    url(r'^(?P<pk>\d+)/$', PostDetail.as_view(), name='post-detail'),
]
