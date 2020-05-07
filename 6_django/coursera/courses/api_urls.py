from rest_framework import routers

from courses import views

router = routers.DefaultRouter()
router.register('', views.CourseAPIViewSet)
urlpatterns = router.urls
