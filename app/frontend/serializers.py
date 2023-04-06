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
from django.conf import settings
from rest_framework.mixins import CreateModelMixin


# абстрактный базовый сериализатор

class AbstractSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source='public_id', read_only=True, format='hex')
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        # kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)
    
   
    

    class Meta:
        abstract = True

class UserSerializer(AbstractSerializer):

    class Meta:
        model = BaseIdeinerUser
        fields = ['username', 'first_name', 'surname', 'email', 'age', 'password', 'is_superuser', 'public_id', 'avatar']
        read_only_field = ['is_active']


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        print('representation')
        print(representation)
        # if not representation['avatar']:
        #     representation['avatar'] = settings.DEFAULT_AUTO_FIELD
        #     return representation
        # if settings.DEBUG: # debug enabled for dev
        #     request = self.context.get('request')
        #     representation['avatar'] = request.build_absolute_uri(representation['avatar'])
        return representation

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['user'] = UserSerializer(self.user).data
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
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
