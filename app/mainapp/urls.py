from django.urls import path, include
import mainapp.views as mainapp
from rest_framework.routers import DefaultRouter
from .views import IdeaModelViewSet, FeedbackModelSerializer

app_name = "mainapp"

router = DefaultRouter()
router.register(r'idea', IdeaModelViewSet, basename='idea')

urlpatterns = [
    path("ideas_list/", mainapp.ideas_list, name="ideas_list"),
    path("idea_add/", mainapp.idea_add, name="idea_add"),
    path("idea_delete/<int:pk>)/", mainapp.idea_delete, name="idea_delete"),
    path("idea_edit/<int:pk>)/", mainapp.idea_edit, name="idea_edit"),
    path("feedback_delete/<int:pk>)/", mainapp.feedback_delete, name="feedback_delete"),
    path("feedback_edit/<int:pk>)/", mainapp.feedback_edit, name="feedback_edit"),
    path("feedback_add/<int:pk>)", mainapp.feedback_add, name="feedback_add"),
    path('api-main/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
