from django.urls import path, include
from django.views.generic import RedirectView

app_name = 'config'

urlpatterns = [
    path("", RedirectView.as_view(url="backend/")),
    path("api/", include("frontend.urls", namespace='api')),
    path("backend/", include("backend.urls", namespace='backend')),
    path("authapp/", include("authapp.urls", namespace='authapp')),
]