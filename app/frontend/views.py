from backend import models
from authapp.models import BaseIdeinerUser

from rest_framework import viewsets
from rest_framework import permissions
from frontend.serializers import IdeaSerializer, FeedbackSerializer, RegisterSerializer, UserSerializer, IssueTokenRequestSerializer, TokenSeriazliser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from frontend.serializers import LoginSerializer

from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework import viewsets
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework.decorators import action
from django.http import Http404
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters

class AbstractViewSet(viewsets.ModelViewSet):
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['updated', 'created']
    ordering = ['-updated']

class UserViewSet(AbstractViewSet):
    http_method_names = ('patch', 'get')
    permission_classes = (AllowAny,) #  IsAuthenticated вернуть после тестироваиня
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return BaseIdeinerUser.objects.all()
        return BaseIdeinerUser.objects.exclude(is_superuser=True)
    
    def get_object(self):
        obj = BaseIdeinerUser.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj

class LoginViewSet(ViewSet):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        return Response(serializer.validated_data, status=status.HTTP_200_OK)



class RefreshViewSet(viewsets.ViewSet, TokenRefreshView):
    permission_classes = (AllowAny,)
    http_method_names = ['post']
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        return Response(serializer.validated_data, status=status.HTTP_200_OK)



class RegisterViewSet(viewsets.ViewSet):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        res = { "refresh": str(refresh),
        "access": str(refresh.access_token), }
        return Response({
            "user": serializer.data,
            "refresh": res["refresh"],
            "token": res["access"]},
            status=status.HTTP_201_CREATED)



class UserPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_anonymous:
            return request.method in SAFE_METHODS
        if view.basename in ["post"]:
            return bool(request.user and request.user.is_authenticated)
        return False
    
    def has_permission(self, request, view):
        if view.basename in ["post"]:
            if request.user.is_anonymous:
                return request.method in SAFE_METHODS
            return bool(request.user and request.user.is_authenticated)
        return False





class IdeaViewSet(AbstractViewSet):
    http_method_names = ('post', 'get', 'put', 'delete')  # ('patch', 'get')
    permission_classes = (permissions.AllowAny,) # IsAuthenticated AllowAny
    # queryset = models.Idea.objects.all()
    serializer_class = IdeaSerializer

    def get_queryset(self):  
        return models.Idea.objects.all() # получаем все временно
        # if self.request.user.is_superuser:
        #     return models.Idea.objects.all()
        # return models.Idea.objects.exclude(is_superuser=True)
    
    def get_object(self):  # получаем один экземпляр
        obj = models.Idea.objects.get_object_by_public_id(self.kwargs['pk'])
        # self.check_object_permissions(self.request, obj)
        return obj
    
    def update(self, instance, validated_data):
        if not instance.edited:
            validated_data['edited'] = True
            instance = super().update(instance, validated_data)
            return instance
        
    @action(methods=['post'], detail=True)
    def like(self, request, *args, **kwargs):
        post = self.get_object()
        user = self.request.user
        user.like(post)
        serializer = self.serializer_class(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=True)
    def remove_like(self, request, *args, **kwargs):
        post = self.get_object()
        user = self.request.user
        user.remove_like(post)
        serializer = self.serializer_class(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class FeedbackViewSet(AbstractViewSet):
    http_method_names = ('post', 'get', 'put', 'delete')
    permission_classes = (AllowAny,)  # UserPermission
    serializer_class = FeedbackSerializer

    def get_queryset(self):
        return models.Feedback.objects.all()  # временно
        # if self.request.user.is_superuser: 
        #     return models.Feedback.objects.all()
        # print('self.kwargs')
        # print(self.kwargs)
        # idea_pk = self.kwargs['idea_pk']
        # if idea_pk is None:
        #     return Http404
        # queryset = models.Feedback.objects.filter(post__public_id=idea_pk)
        # return queryset
    
    def get_object(self):
        obj = models.Feedback.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def validate_post(self, value):
        if self.instance:
            return self.instance.post
        return value

class JoinedUsersViewSet(AbstractViewSet):
    queryset = models.JoinedUsers.objects.all()
    serializer_class = IdeaSerializer
    # permission_classes = [permissions.IsAuthenticated]

class LikesViewSet(AbstractViewSet):
    queryset = models.LikesToIdeas.objects.all()
    serializer_class = IdeaSerializer
    # permission_classes = [permissions.IsAuthenticated]


