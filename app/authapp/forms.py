from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm

from .models import ShopUser


class ShopUserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(ShopUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = ShopUser
        fields = ("username", "password")


class ShopUserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(ShopUserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.help_text = ""

    class Meta:
        model = ShopUser
        fields = ("username", "first_name", "surname", "email", "password1", "password2", "avatar")


class ShopUserEditForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(ShopUserEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.help_text = ""

    class Meta:
        model = ShopUser
        fields = ("username", "first_name", "surname", "email", "password", "avatar")
