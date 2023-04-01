from django.urls import include, path
from rest_framework import routers
from frontend import views

app_name = 'frontend'

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='users')
router.register(r'ideas', views.IdeaViewSet, basename='ideas')
router.register(r'jusers', views.JoinedUsersViewSet, basename='jusers')
router.register(r'likes', views.LikesViewSet, basename='likes')
router.register(r'feedback', views.FeedbackViewSet, basename='feedback')
router.register(r'register', views.RegisterViewSet, basename='register'),
router.register(r'login', views.LoginViewSet, basename='login'),
router.register(r'refresh', views.RefreshViewSet, basename='refresh'),

urlpatterns = [
    path('', include(router.urls), name='api'),

]