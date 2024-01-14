from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Alumni API",
        default_version='v1',
        description="APIs for cuusinhvien",
        contact=openapi.Contact(email="lochuynh2510@gmail.com"),
        license=openapi.License(name="Huỳnh Hữu Lộc@2023"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('alumni.urls')),
    path('o/', include('oauth2_provider.urls',
                       namespace='oauth2_provider')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
    schema_view.without_ui(cache_timeout=0),
    name='schema-json'),
    re_path(r'^swagger/$',
    schema_view.with_ui('swagger', cache_timeout=0),
    name='schema-swagger-ui'),
    re_path(r'^redoc/$',
    schema_view.with_ui('redoc', cache_timeout=0),
    name='schema-redoc')
]