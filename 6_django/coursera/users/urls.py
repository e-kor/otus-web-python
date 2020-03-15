from django.urls import path

import users.views as views

app_name = 'users'
urlpatterns = [
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('login', views.login, name='login'),
]
