from django.urls import path
import courses.views as views
from courses.views import CourseListView
app_name = 'users'
urlpatterns = [
    path('', views.CourseListView.as_view(), name='edit'),
    path('', views.CourseListView.as_view(), name='logout'),

    path('', views.CourseListView.as_view(), name='login'),
]