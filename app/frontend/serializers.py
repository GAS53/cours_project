from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.exceptions import ValidationError

from backend import models
from authapp.models import BaseIdeinerUser


# абстрактный базовый сериализатор

class AbstractSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source='public_id', read_only=True, format='hex')
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)



    class Meta:
        abstract = True

class UserSerializer(AbstractSerializer):

    class Meta:
        model = BaseIdeinerUser
        fields = ['username', 'first_name', 'surname', 'email', 'age', 'password', 'is_superuser']
        read_only_field = ['is_active']


    # def create(self, request, *args, **kwargs):
    #     print('request.data')
    #     print(request)
    #     serializer = self.get_serializer(data=request.data) 
    #     print('request.data error')
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    
# регистрация и валидация

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        print(f'dddddddddddddddddddddddd {data}')
        refresh = self.get_token(self.user)
        data['user'] = UserSerializer(self.user).data
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        print(f'ddd {data}')
        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)
        return data


class IssueTokenRequestSerializer(serializers.Serializer):
    model = BaseIdeinerUser

    nickname = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class TokenSeriazliser(serializers.ModelSerializer):

    class Meta:
        model = Token
        fields = ['key']

class RegisterSerializer(UserSerializer):
    password = serializers.CharField(max_length=128,
        min_length=8, write_only=True, required=True)
    
    class Meta:
        model = BaseIdeinerUser
        fields = ['id', 'email', 'username',
            'first_name', 'surname', 'password']
        
    def create(self, validated_data):
        return BaseIdeinerUser.objects.create_user(**validated_data)


# сериализаторы основных таблиц


class IdeaSerializer(AbstractSerializer):
    liked = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = models.Idea
        fields = ['autor', 'title', 'rubrics', 'created', 'preview', 'body', 'liked', 'likes_count', 'created', 'updated']
        read_only_fields = ["edited"]

    def get_queryset(self):
        return models.Idea.objects.all()
    
    def get_object(self):
        obj = models.Idea.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj

    def create(self, request, *args, **kwargs):
        print('request.data')
        print(request)
        serializer = self.get_serializer(data=request.data) # data=request.data т.к передаю не полноценный запрос
        
        print('request.data error')
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get_liked(self, instance):
        request = self.context.get('request', None)
        if request is None or request.user.is_anonymous:
            return False
        return request.user.has_liked(instance)
    
    def get_likes_count(self, instance):
        return instance.liked_by.count()


class FeedbackSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(queryset=BaseIdeinerUser.objects.all(), slug_field='public_id')
    idea = serializers.SlugRelatedField(queryset = models.Idea.objects.all(), slug_field='public_id')
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        author = BaseIdeinerUser.objects.get_object_by_public_id(rep["author"])
        rep["author"] = UserSerializer(author).data
        return rep
    
    class Meta:
        model = models.Feedback
        fields = ['id', 'author', 'idea', 'rating', 'feedback', 'created', 'updated']
        read_only_fields = ["edited"]

    def validate_author(self, value):
        if self.context["request"].user != value:
            raise ValidationError("вы не можете создать пост за другого пользователя")
        return value



    def update(self, instance, validated_data):
        if not instance.edited:
            validated_data['edited'] = True
        instance = super().update(instance,  validated_data)
        return instance


class JoinedUsersSerializer(AbstractSerializer):
    class Meta:
        model = models.JoinedUsers
        fields = ['idea', 'autor']

class LikesSerializer(AbstractSerializer):
    class Meta:
        model = models.LikesToIdeas
        fields = ['idea', 'autor']