from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework.authtoken import views


app_name = 'config'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", RedirectView.as_view(url="mainapp/")),
    path("mainapp/", include("mainapp.urls", namespace='mainapp')),
    path("authn/", include("authnapp.urls", namespace='auth')),
    path("apiapp/", include("apiapp.urls", namespace='apiapp')),
    path('api-token-auth/', views.obtain_auth_token)
]
