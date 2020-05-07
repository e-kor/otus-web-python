from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from graphene_django.views import GraphQLView
from rest_framework import permissions

from .schema import schema

api_urls = [
    path('api/courses/', include('courses.api_urls')),
    path('api/auth/', include('users.api_urls')),
    path('api/misc/', include('misc.urls')),
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
    path("graphql/", GraphQLView.as_view(graphiql=True, schema=schema)),

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [url(r'^silk/', include('silk.urls', namespace='silk'))]
    urlpatterns += [path('__debug__/',
                         include(debug_toolbar.urls)), ]
