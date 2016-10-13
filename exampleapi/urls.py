from django.conf.urls import include, url
from django.contrib import admin

import api_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api_urls)),
]
