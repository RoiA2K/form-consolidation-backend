from django.urls import path
from rest_framework.routers import DefaultRouter

from api import views
from api.views import FormsViewSet, FormFieldsViewSet, UsersViewSet, UserRegisterView, UserLoginView, FormTemplateView, FormTemplateDetailView
from drf_spectacular.views import SpectacularRedocView, SpectacularSwaggerView

router = DefaultRouter()
router.register(
    'users', UsersViewSet, basename='users'
)
router.register(
    'forms', FormsViewSet, basename='forms'
)
router.register(
    'formfields', FormFieldsViewSet, basename='formfields'
)

urlpatterns = [
    path('register/', UserRegisterView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('ftemplates/', FormTemplateView.as_view()),
    path('ftemplates/<int:pk>/', FormTemplateDetailView.as_view(), name='form-template-detail'),

    # Optional UI:
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc')
]+router.urls
