from django.conf import settings
from django.conf.urls import include, url
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer

from rest_framework import permissions, response, schemas
from rest_framework.decorators import (api_view, permission_classes,
                                       renderer_classes)

urlpatterns = [
    url(r'^news/', include('news.urls')),
    url(r'^tags/', include('tags.urls')),
]


@api_view()
@permission_classes([permissions.AllowAny])
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='Example API')
    return response.Response(generator.get_schema(request=request))

urlpatterns += [url(r'^docs/',
                schema_view)]
