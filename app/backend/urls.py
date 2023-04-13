from django.urls import path

import backend.views as backend

app_name = 'backend'

urlpatterns = [
    path("", backend.main, name="index"),
    path("idea_card/<uuid:pk>/", backend.idea_card, name="idea_card"),
    path("lk", backend.lk, name="lk"),
    path("lk_edit", backend.lk_edit, name="lk_edit"),
    path("admin/", backend.admin, name="admin"),
    path("search/", backend.search, name="search"),
    path("my_ideas/", backend.my_ideas, name="my_ideas"),
    path("idea_add/", backend.idea_add, name="idea_add"),
    path("idea_delete/<uuid:pk>/", backend.idea_delete, name="idea_delete"),
    path("idea_card_delete/<uuid:pk>/", backend.idea_card_delete, name="idea_card_delete"),
    path("idea_edit/<uuid:pk>/", backend.idea_edit, name="idea_edit"),
    path("feedback_delete/<uuid:pk>/", backend.feedback_delete, name="feedback_delete"),
    path("feedback_edit/<uuid:pk>/", backend.feedback_edit, name="feedback_edit"),
    path("feedback_add/<uuid:pk>", backend.feedback_add, name="feedback_add"),
    path("joined_user_delete/<uuid:pk>/", backend.joined_user_delete, name="joined_user_delete"),
    path("joined_user_add/<uuid:pk>", backend.joined_user_add, name="joined_user_add"),
    path("like_delete/<uuid:pk>/", backend.like_delete, name="like_delete"),
    path("like_add/<uuid:pk>", backend.like_add, name="like_add"),
]
