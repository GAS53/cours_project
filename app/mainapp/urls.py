from django.urls import path
from mainapp import views
from django.views.generic import RedirectView

app_name = 'mainapp'

urlpatterns = [
    path("", RedirectView.as_view(url="index/")),
    path("index/", views.Temp.as_view(), name="index"),


    ]