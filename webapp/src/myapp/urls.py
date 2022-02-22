from rest_framework.routers import DefaultRouter

from myapp.views import UserRegistration

urlpatterns = []


router = DefaultRouter()
router.register('cat', UserRegistration, basename='cat')

urlpatterns += router.urls
