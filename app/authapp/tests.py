# 1. Тест на создание пользователя

from django.test import TestCase
from authapp.models import BaseIdeinerUser

class UserModelTestCase(TestCase):
    def setUp(self):
        self.user = BaseIdeinerUser.objects.create_user(
            login='testuser',
            email='testuser@mail.com',
            password='testpassword'
        )

    def test_user_creation(self):
        self.assertTrue(isinstance(self.user, BaseIdeinerUser))
        self.assertEqual(self.user.__str__(), self.user.login)
        self.assertEqual(self.user.email, 'testuser@mail.com')
        self.assertTrue(self.user.check_password('testpassword'))


# 2. Тест на изменение пароля пользователя

from django.test import TestCase
from authapp.models import BaseIdeinerUser

class UserModelTestCase(TestCase):
    def setUp(self):
        self.user = BaseIdeinerUser.objects.create_user(
            login='testuser',
            email='testuser@mail.com',
            password='testpassword'
        )

    def test_change_password(self):
        self.user.set_password('newpassword')
        self.assertTrue(self.user.check_password('newpassword'))


# 3. Тест на получение пользователя по public_id

from django.test import TestCase
from authapp.models import BaseIdeinerUser

class UserModelTestCase(TestCase):
    def setUp(self):
        self.user = BaseIdeinerUser.objects.create_user(
            login='testuser',
            email='testuser@mail.com',
            password='testpassword'
        )

    def test_get_user_by_public_id(self):
        user = BaseIdeinerUser.objects.get_object_by_public_id(self.user.public_id)
        self.assertEqual(user, self.user)


# 4. Тест на генерацию JWT токена

from django.test import TestCase
from authapp.models import BaseIdeinerUser

class UserModelTestCase(TestCase):
    def setUp(self):
        self.user = BaseIdeinerUser.objects.create_user(
            login='testuser',
            email='testuser@mail.com',
            password='testpassword'
        )

    def test_jwt_token_generation(self):
        token = self.user.generate_jwt_token()
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        self.assertEqual(decoded_token['public_id'], str(self.user.public_id))


# 5. Тест на проверку прав доступа пользователя

from django.test import TestCase
from authapp.models import BaseIdeinerUser

class UserModelTestCase(TestCase):
    def setUp(self):
        self.user = BaseIdeinerUser.objects.create_user(
            login='testuser',
            email='testuser@mail.com',
            password='testpassword'
        )

    def test_user_permissions(self):
        self.assertEqual(self.user.is_superuser, False)
        self.assertEqual(self.user.is_staff, False)
        self.assertEqual(self.user.is_active, True)

