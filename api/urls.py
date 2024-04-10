from django.urls import path
from rest_framework.routers import DefaultRouter

from api import views
from api.views import FormsViewSet, UsersViewSet

router = DefaultRouter()
router.register(
    'users', UsersViewSet, basename='users'
)
router.register(
    'forms', FormsViewSet, basename='forms'
)

urlpatterns = [
]+router.urls
