from django.urls import path, include
import authnapp.views as authnapp
from rest_framework.routers import DefaultRouter
from .views import ShopUserModelViewSet

app_name = "authnapp"

router = DefaultRouter()
router.register('Users', ShopUserModelViewSet)

urlpatterns = [
    path("login/", authnapp.login, name="login"),
    path("logout/", authnapp.logout, name="logout"),
    path("register/", authnapp.register, name="register"),
    path("edit/", authnapp.edit, name="edit"),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
