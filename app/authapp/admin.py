from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import BaseIdeinerUser


class BaseIdeinerUserAdmin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "age"),
            },
        ),
    )


admin.site.register(BaseIdeinerUser, BaseIdeinerUserAdmin)
