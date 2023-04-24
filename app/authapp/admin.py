from django.contrib import admin

from authapp.models import BaseIdeinerUser

# Register your models here.
# admin.site.register(BaseIdeinerUser)

@admin.register(BaseIdeinerUser)  # регистрация
class UserAdmin(admin.ModelAdmin):
    # list_display значения которые будут видны на экране
    # list_display = ['id','get_course_name', 'title', 'deleted', 'created'] # поля из табилц mainapp_models.News
    # ordering = ['-name__cost', 'description'] # Сортировка задаётся и по связным полям, что указывается через __ (двойное подчёркивание)
    list_per_page = 4 # максимальное количество на странице иначе пагинатор
    # list_filter = ['deleted','description_as_markdown'] # отображение фильтров сбоку для удобного выбора
    # search_fields = ['description', 'name'] # поля в которых искать
    actions = ['mark_deleted'] # задать действия с несколькими выбранными новостями
