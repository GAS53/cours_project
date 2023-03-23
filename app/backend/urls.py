from backend import views
from django.views.generic import RedirectView
from django.urls import path, include
import backend.views as backend
from rest_framework.routers import DefaultRouter
from .views import IdeaModelViewSet


app_name = 'backend'

router = DefaultRouter()
router.register(r'idea', IdeaModelViewSet, basename='idea')

urlpatterns = [
    path("", RedirectView.as_view(url="index/")),
    path("index/", backend.ideas_list, name="index"),
    path("idea_add/", backend.idea_add, name="idea_add"),
    path("idea_delete/<int:pk>)/", backend.idea_delete, name="idea_delete"),
    path("idea_edit/<int:pk>)/", backend.idea_edit, name="idea_edit"),
    path("feedback_delete/<int:pk>)/", backend.feedback_delete, name="feedback_delete"),
    path("feedback_edit/<int:pk>)/", backend.feedback_edit, name="feedback_edit"),
    path("feedback_add/<int:pk>)", backend.feedback_add, name="feedback_add"),
    path("joined_user_delete/<int:pk>)/", backend.joined_user_delete, name="joined_user_delete"),
    path("joined_user_add/<int:pk>)", backend.joined_user_add, name="joined_user_add"),
    path('api-main/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]