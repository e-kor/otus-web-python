from django.urls import path
import courses.views as views
app_name = 'courses'
urlpatterns = [
    path('', views.CourseListView.as_view(), name='index'),]