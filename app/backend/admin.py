from django.contrib import admin

from backend.models import Rubric, Idea, Feedback, JoinedUser, LikesToIdea

# Register your models here.
admin.site.register(Rubric)
admin.site.register(Idea)
admin.site.register(Feedback)
admin.site.register(JoinedUser)
admin.site.register(LikesToIdea)
