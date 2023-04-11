from backend import models
from authapp.models import BaseIdeinerUser

from rest_framework import viewsets, status, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework import filters

import frontend.serializers as fr_serializers
import backend.models as bk_models
from authapp.models import BaseIdeinerUser


class AbstractViewSet(viewsets.ModelViewSet):
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['updated', 'created']
    ordering = ['-updated']


class MakeNewUeser(AbstractViewSet):
    http_method_names = ('post')
    permission_classes = (AllowAny,)
    serializer_class = fr_serializers.NewUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class MinIdeasViewSet(AbstractViewSet):
    http_method_names = ('get')
    permission_classes = (AllowAny,) 
    serializer_class = fr_serializers.MinIdesSerializer


    def get_queryset(self):
        return bk_models.Idea.objects.all() 



class LoginViewSet(AbstractViewSet):
    serializer_class = fr_serializers.LoginSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class OneIdeaViewSet(AbstractViewSet):
    serializer_class = fr_serializers.OneIdeaSerializer
    permission_classes = (AllowAny,) # IsAuthenticated  исправить когда django примет токен
    http_method_names = ['get']

    def get_object(self):
        obj = bk_models.Idea.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj
    

class JoinToIdea(AbstractViewSet):
    serializer_class = fr_serializers.LoginSerializer
    permission_classes = (AllowAny,)   # IsAuthenticated  исправить когда django примет токен
    http_method_names = ['patch']

    def get_object(self, pk):
        return bk_models.JoinedUser.objects.get(pk=pk)

    def patch(self, request):
        print('request')
        print(request.data)
        join_object = self.objects.get_object_by_public_id(request.data['pk'])
        serializer = fr_serializers.JoinedUserSerializer(join_object, data=request.DATA, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(code=201, data=serializer.data)
        return Response(code=400, data="неправильно заданы параметры, ошибка при серриализации")






























class UserViewSet(AbstractViewSet):
    http_method_names = ('patch', 'get')
    permission_classes = (AllowAny,) #  IsAuthenticated вернуть после тестироваиня
    serializer_class = fr_serializers.UserSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return BaseIdeinerUser.objects.all()
        return BaseIdeinerUser.objects.exclude(is_superuser=True)
    
    def get_object(self):
        obj = BaseIdeinerUser.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)







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
    serializer_class = fr_serializers.RegisterSerializer
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
    http_method_names = ('post', 'get', 'put', 'delete')
    permission_classes = (AllowAny,)  # UserPermission
    serializer_class = fr_serializers.IdeaSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        return bk_models.Idea.objects.all() 
        
    def get_object(self):
        obj = bk_models.Idea.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj

    def validate_post(self, value):
        if self.instance:
            return self.instance.post
        return value




class NewRubricViewSet(AbstractViewSet):
    http_method_names = ('post',)
    permission_classes = (AllowAny,)  # UserPermission !!!!!!!!!!!
    serializer_class = fr_serializers.RubricSerializer


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        res = self.perform_create(serializer)
        if res:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_304_NOT_MODIFIED)

    def perform_create(self, serializer):
        new_rubric = self.request.data.get("rubirc_name", None) # read data from request
        preparate_qs =[val[-1] for val in bk_models.Rubric.objects.all().values_list()]
        if new_rubric in preparate_qs:
            return False
        else:
            serializer.save()
            return True


class AllRubricsViewSet(AbstractViewSet):
    http_method_names = ('get',)
    permission_classes = (AllowAny,)  # UserPermission !!!!!!!!!!!
    serializer_class = fr_serializers.RubricSerializer


    def get_queryset(self):
        return bk_models.Rubric.objects.all()











class RubricViewSet(AbstractViewSet):
    http_method_names = ('post', 'get', 'put', 'delete')
    permission_classes = (AllowAny,)  # UserPermission
    serializer_class = fr_serializers.RubricSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        return bk_models.Rubric.objects.all() 
        
    def get_object(self):
        obj = bk_models.Rubric.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj
    
    def validate_rubric(self, value):
        if self.instance:
            return self.instance.rubric
        return value



class FeedbackViewSet(AbstractViewSet):
    http_method_names = ('post', 'get', 'put', 'delete')
    permission_classes = (AllowAny,)  # UserPermission
    serializer_class = fr_serializers.FeedbackSerializer

    def get_queryset(self):
        return models.Feedback.objects.all()  # временно
        # if self.request.user.is_superuser: 
        #     return models.Feedback.objects.all()
        # print('self.kwargs')
        # print(self.kwargs)
        # idea_pk = self.kwargs['public_id']
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



class JoinedUserViewSet(AbstractViewSet):
    http_method_names = ('post', 'get', 'put', 'delete')
    permission_classes = (AllowAny,)  # UserPermission
    serializer_class =  fr_serializers.JoinedUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        return bk_models.JoinedUser.objects.all() 
        
    def get_object(self):
        obj = bk_models.JoinedUser.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj

    def validate_post(self, value):
        if self.instance:
            return self.instance.post
        return value


class LikesViewSet(AbstractViewSet):
    http_method_names = ('post', 'get', 'put', 'delete')
    permission_classes = (AllowAny,)  # UserPermission
    serializer_class = fr_serializers.LikesSerializer


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        return bk_models.LikesToIdea.objects.all() 
        
    def get_object(self):
        obj = bk_models.LikesToIdea.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj

    def validate_post(self, value):
        if self.instance:
            return self.instance.post
        return value