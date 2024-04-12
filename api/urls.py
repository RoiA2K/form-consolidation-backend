from django.urls import path
from rest_framework.routers import DefaultRouter

from api import views
from api.views import FormsViewSet, UsersViewSet, UserRegisterView, UserLoginView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

router = DefaultRouter()
router.register(
    'users', UsersViewSet, basename='users'
)
router.register(
    'forms', FormsViewSet, basename='forms'
)

urlpatterns = [
    path('register/', UserRegisterView.as_view()),
    path('login/', UserLoginView.as_view()),

    # Optional UI:
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc')
]+router.urls
