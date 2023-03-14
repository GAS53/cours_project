from django.urls import path, include
import mainapp.views as mainapp
from rest_framework.routers import DefaultRouter
from .views import IdeaModelViewSet

app_name = "mainapp"

router = DefaultRouter()
router.register('idea', IdeaModelViewSet)

urlpatterns = [
    path("ideas_list/", mainapp.ideas_list, name="ideas_list"),
    path("idea_add/", mainapp.idea_add, name="idea_add"),
    path("idea_delete/<int:pk>)/", mainapp.idea_delete, name="idea_delete"),
    path("idea_edit/<int:pk>)/", mainapp.idea_edit, name="idea_edit"),
    path('api-main/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
