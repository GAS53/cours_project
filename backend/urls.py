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
    path("", backend.main, name="index"),
    path("idea_card/<int:pk>/", backend.idea_card, name="idea_card"),
    path("lk/", backend.lk, name="lk"),
    path("lk_edit/", backend.lk_edit, name="lk_edit"),
    path("admin/", backend.admin, name="admin"),
    path("search/", backend.search, name="search"),
    path("my_ideas/", backend.my_ideas, name="my_ideas"),
    path("idea_add/", backend.idea_add, name="idea_add"),
    path("idea_delete/<int:pk>/", backend.idea_delete, name="idea_delete"),
    path("idea_card_delete/<int:pk>/", backend.idea_card_delete, name="idea_card_delete"),
    path("idea_edit/<int:pk>/", backend.idea_edit, name="idea_edit"),
    path("feedback_delete/<int:pk>/", backend.feedback_delete, name="feedback_delete"),
    path("feedback_edit/<int:pk>/", backend.feedback_edit, name="feedback_edit"),
    path("feedback_add/<int:pk>", backend.feedback_add, name="feedback_add"),
    path("joined_user_delete/<int:pk>/", backend.joined_user_delete, name="joined_user_delete"),
    path("joined_user_add/<int:pk>", backend.joined_user_add, name="joined_user_add"),
    path("like_delete/<int:pk>/", backend.like_delete, name="like_delete"),
    path("like_add/<int:pk>", backend.like_add, name="like_add"),
    path('api-main/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]