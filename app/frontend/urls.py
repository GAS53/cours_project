from django.urls import include, path
from rest_framework import routers
from frontend import views

app_name = 'frontend'

router = routers.DefaultRouter()
router.register(r'new_user', views.MakeNewUeser, basename='new_user')
router.register(r'ideas', views.MinIdeasViewSet, basename='ideas')
router.register(r'idea', views.GetIdeaViewSet, basename='idea')
router.register(r'new_idea', views.PostIdeaViewSet, basename='new_idea')
router.register(r'join', views.JoinToIdea, basename='join')
router.register(r'new_rubric', views.NewRubricViewSet, basename='new_rubric')
router.register(r'rubrics', views.AllRubricsViewSet, basename='rubrics')
router.register(r'like', views.LikesViewSet, basename='like')
router.register(r'login', views.LoginViewSet, basename='login'),
router.register(r'refresh', views.RefreshViewSet, basename='refresh'),




# router.register(r'users', views.UserViewSet, basename='users')
# router.register(r'rubrics', views.RubricViewSet, basename='rubrics')
# router.register(r'ideas', views.IdeaViewSet, basename='ideas')
# router.register(r'jusers', views.JoinedUserViewSet, basename='jusers')
# router.register(r'likes', views.LikesViewSet, basename='likes')
# router.register(r'feedback', views.FeedbackViewSet, basename='feedback')
router.register(r'register', views.RegisterViewSet, basename='register'),


urlpatterns = [
    path('', include(router.urls), name='api'),

]
