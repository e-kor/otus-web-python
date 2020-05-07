from django.urls import path

from misc.views import send_feedback

urlpatterns = [
    path('feedback/', send_feedback, name='send feedback to admins')]
