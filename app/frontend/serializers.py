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
from backend import models as backend


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
        fields = ['login', 'first_name', 'last_name', 'email', 'age', 'password', 'is_superuser', 'public_id', 'avatar']
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
        fields = ['id', 'email', 'login',
            'first_name', 'last_name', 'password']
        
    def create(self, validated_data):
        return BaseIdeinerUser.objects.create_user(**validated_data)

class RubricSerializer(AbstractSerializer):
   
    class Meta:
        model = backend.Rubric
        fields = ['id', 'rubirc_name']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        return rep
    
    def update(self, instance, validated_data):
        if not instance.edited:
            validated_data['edited'] = True
        instance = super().update(instance,  validated_data)
        return instance





# сериализаторы основных таблиц
from backend.models import Idea

class IdeaSerializer(AbstractSerializer):
    autor = serializers.SlugRelatedField(queryset=BaseIdeinerUser.objects.all(), slug_field='public_id')
    rubric = serializers.SlugRelatedField(queryset = models.Rubric.objects.all(), slug_field='public_id')
    
    class Meta:
        model = backend.Idea
        fields = ['id', 'autor', 'title', 'rubric', 'preview', 'body']


    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["rubric"] = RubricSerializer().data
        rep["autor"] = UserSerializer().data
        return rep
    
    def update(self, instance, validated_data):
        if not instance.edited:
            validated_data['edited'] = True
        instance = super().update(instance,  validated_data)
        return instance
        


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


class JoinedUserSerializer(AbstractSerializer):
    class Meta:
        model = models.JoinedUser
        fields = ['id', 'idea', 'user']

class LikesSerializer(AbstractSerializer):
    class Meta:
        model = models.LikesToIdea
        fields = ['id', 'idea', 'autor']

