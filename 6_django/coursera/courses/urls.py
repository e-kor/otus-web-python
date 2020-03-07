from django.urls import path

from courses import views

app_name = 'courses'
urlpatterns = [
    path('thankyou/', views.thankyou, name='thankyou'),
    path('', views.CourseListView.as_view(), name='index'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('course/detail/<int:pk>/', views.CourseDetailView.as_view(),
         name='course'),
    path('course/create/', views.CourseCreateView.as_view(),
         name='course_create'),
    path('course/update/<int:pk>/', views.CourseUpdateView.as_view(),
         name='course_update'),
    path('course/delete/<int:pk>/', views.CourseDeleteView.as_view(),
         name='course_delete'),
]
