from django.conf.urls import url

from tags.views import TagList, TagDetail

urlpatterns = [
    url(r'^$', TagList.as_view(), name='tag-list'),
    url(r'^(?P<pk>\d+)/$', TagDetail.as_view(), name='tag-detail'),
]
