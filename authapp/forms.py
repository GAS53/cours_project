from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm

from .models import BaseIdeinerUser


class BaseIdeinerUserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(BaseIdeinerUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = BaseIdeinerUser
        fields = ("email", "password")


class BaseIdeinerUserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(BaseIdeinerUserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.help_text = ""

    class Meta:
        model = BaseIdeinerUser
        fields = ("login", "first_name", "last_name", "email", "password1", "password2", "avatar")


class BaseIdeinerUserEditForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(BaseIdeinerUserEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.help_text = ""

    class Meta:
        model = BaseIdeinerUser
        fields = ("login", "first_name", "last_name", "email", "password", "avatar")
