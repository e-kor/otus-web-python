from django.contrib import admin
from django.urls import path
from django.urls import path, include, re_path
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courses.urls', namespace='courses')),
    path('users/', include('users.urls', namespace='users')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns