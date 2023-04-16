from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login

from rest_framework import serializers
from rest_framework.exceptions import ValidationError


from authapp.models import BaseIdeinerUser
from django.conf import settings

from backend import models as backend


# абстрактный базовый сериализатор

class AbstractSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True, format='hex')
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    class Meta:
        abstract = True


class NewUserSerializer(AbstractSerializer):

    class Meta:
        model = BaseIdeinerUser
        fields = ['login', 'first_name', 'last_name', 'email', 'age', 'password', 'id', 'avatar']
        read_only_field = ['is_active']

    def create(self, validated_data):
        user = BaseIdeinerUser(
            email=validated_data['email'],
            login=validated_data['login'],
            age = validated_data['age'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user



class MinIdesSerializer(AbstractSerializer):
    class Meta:
        model = backend.Idea
        fields = ['id', 'rubric', 'title', 'preview' ]
        read_only_fields = ["edited"]



class UserSerializer(AbstractSerializer):
    '''вложенные методы не проверены'''
    class Meta:
        model = BaseIdeinerUser
        fields = ['id', 'login', 'first_name', 'last_name', 'email', 'age', 'password', 'is_superuser', 'id', 'avatar']
        read_only_field = ['is_active']


    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # if not representation['avatar']:
        #     representation['avatar'] = settings.DEFAULT_AUTO_FIELD
        #     return representation
        # if settings.DEBUG: # debug enabled for dev
        #     request = self.context.get('request')
        #     representation['avatar'] = request.build_absolute_uri(representation['avatar'])
        return representation

class RubricSerializer(AbstractSerializer):
    '''вложенные методы не проверены'''
    class Meta:
        model = backend.Rubric
        fields =  ['id', 'rubirc_name']

    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     return rep
    
    # def update(self, instance, validated_data):
    #     if not instance.edited:
    #         validated_data['edited'] = True
    #     instance = super().update(instance,  validated_data)
    #     return instance

class JoinedUserSerializer(AbstractSerializer):
    
    
    class Meta:
        model = backend.JoinedUser
        fields = '__all__' # ['id', 'idea', 'user']

class LikesSerializer(AbstractSerializer):
    class Meta:
        model = backend.LikesToIdea
        fields = '__all__' #['id', 'idea', 'autor']



class FeedbackSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(queryset=BaseIdeinerUser.objects.all(), slug_field='id')
    idea = serializers.SlugRelatedField(queryset = backend.Idea.objects.all(), slug_field='id')
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        author = BaseIdeinerUser.objects.get_object_by_public_id(rep["author"])
        rep["author"] = UserSerializer(author).data
        return rep
    
    class Meta:
        model = backend.Feedback
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




class GetIdeaSerializer(AbstractSerializer):
    autor = UserSerializer()
    rubric = RubricSerializer()
    joinedUser = JoinedUserSerializer(many=True)
    likesToIdea = LikesSerializer(many=True)
    feedback = FeedbackSerializer(many=True)


    class Meta:
        model = backend.Idea
        fields = '__all__'

class PostIdeaSerializer(AbstractSerializer):

    class Meta:
        model = backend.Idea
        fields = '__all__'


















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







# сериализаторы основных таблиц
from backend.models import Idea, Rubric

class IdeaSerializer(AbstractSerializer):
    autor = UserSerializer()
    rubric = RubricSerializer()

    class Meta:
        model = backend.Idea
        fields = ['id', 'autor', 'title', 'rubric', 'preview', 'body']


    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     rep["rubric"] = RubricSerializer().data
    #     rep["autor"] = UserSerializer().data
    #     return rep
    
    def create(self, validated_data):
        profile_data = validated_data.pop('autor')
        user = BaseIdeinerUser.objects.create(**validated_data)
        UserSerializer.objects.create(user=user, **profile_data)

        rubric_data = validated_data.pop('rubric')
        rubric = Rubric.objects.create(**validated_data)
        RubricSerializer.objects.create(rubric=rubric, **rubric_data)
        return user


    
    def update(self, instance, validated_data):
        if not instance.edited:
            validated_data['edited'] = True
        instance = super().update(instance,  validated_data)
        return instance
        






