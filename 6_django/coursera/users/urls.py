from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

import users.views as views

app_name = 'users'
urlpatterns = [
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('login', views.login, name='login'),
]
