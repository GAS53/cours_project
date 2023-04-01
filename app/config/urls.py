<<<<<<< HEAD
=======
from django.contrib import admin
>>>>>>> BW
from django.urls import path, include
from django.views.generic import RedirectView

app_name = 'config'

urlpatterns = [
<<<<<<< HEAD
    path("", RedirectView.as_view(url="backend/")),
    path("api/", include("frontend.urls", namespace='api')),
=======
    path('admin/', admin.site.urls),
    path("", RedirectView.as_view(url="backend/")),
    path("frontend/", include("frontend.urls", namespace='frontend')),
>>>>>>> BW
    path("backend/", include("backend.urls", namespace='backend')),
    path("authapp/", include("authapp.urls", namespace='authapp')),
]