from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

api_urls = [
    path('api/', include('courses.api_urls')),
    path('api/', include('users.api_urls')),
]

schema_view = get_schema_view(
    openapi.Info(
        title="Coursera API",
        default_version='v1',
        contact=openapi.Contact(email="turokg@yahoo.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=api_urls,

)
urlpatterns = api_urls + [
    url('api/schema', schema_view.with_ui('swagger', cache_timeout=0)),
    path('admin/', admin.site.urls),
    path('', include('courses.urls', namespace='courses')),
    path('users/', include('users.urls', namespace='users')),


]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path('__debug__/',
                        include(debug_toolbar.urls)), ] + urlpatterns
