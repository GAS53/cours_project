
import uuid

from django.contrib.auth.models import  AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.contrib.auth.validators import UnicodeUsernameValidator

from backend import models as back_models

# " все картинки загружаются в папку users_avatars. она создаётся авытоматически, но можно её переместить в другую папку, " \
# " например, в static/img, но тогда надо переписать путь:" \
# " upload_to='static/img/users_avatars' "

""" !!!! важно !!!! в файле settings нельзя удалять поле: AUTH_USER_MODEL = 'authapp.BaseIdeinerUser' """
class UserManager(BaseUserManager):
    'добавлено для JWT Tokena'
    def get_object_by_public_id(self, id):
        try:
            instance = self.get(id=id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404

    def create_user(self, login, email, password=None, **kwargs):
        if login is None:
            raise TypeError('Должен быть задан логин')
        if email is None:
            raise TypeError('Должен быть задан email')
        if password is None:
            raise TypeError('Должен быть задан пароль')
        user = self.model(login=login,
        email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, login, email, password, **kwargs):
        if login is None:
            raise TypeError('Должен быть задан логин')
        if email is None:
            raise TypeError('Должен быть задан email')
        if password is None:
            raise TypeError('Должен быть задан пароль')
        user = self.create_user(login, email, password,
        **kwargs)
        user.is_superuser = True
        # user.is_staff = True
        user.save(using=self._db)
        return user
    
def path_to_avatars(instance, filename):
        return 'user_{0}/{1}'.format(instance.id, filename)

# заменен  AbstractUser т.к. перезаписываются поля дублировние при наследовании
class BaseIdeinerUser(AbstractBaseUser, PermissionsMixin): 
    login_validator = UnicodeUsernameValidator()

    id = models.UUIDField(db_index=True, primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    age = models.PositiveIntegerField(verbose_name="возраст", default=18)
    email = models.CharField(verbose_name="email", max_length=40, default="", unique=True)
    login = models.CharField(validators=[login_validator], verbose_name="логин", max_length=40, unique=True, default="")
    last_name = models.CharField(verbose_name="фамилия", max_length=40, default="")
    first_name = models.CharField(verbose_name="имя", max_length=40, default="")
    avatar = models.ImageField(upload_to=path_to_avatars, blank=True, default="")
    password = models.CharField(verbose_name="password", max_length=40, default="")
    registration_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def like(self, post):
        """Лайкнуть не лайкнутую идею"""
        return self.posts_liked.add(post)
    
    def remove_like(self, post):
        """Убрать лайк от идеи"""
        return self.posts_liked.remove(post)
    
    def has_liked(self, post):
        """Проверка лайкнута ли пользователем идея"""
        return self.posts_liked.filter(pk=post.pk).exists()



    def __str__(self):
        return f"{self.login} ({self.password})"
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['login']

    @property
    def name(self):
        return f"{self.login} {self.first_name}"
    
    objects = UserManager()


    




