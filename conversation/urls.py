from django.urls import path
from . import views

app_name = "conversation"

urlpatterns = [
    path("", views.conversation_list, name="conversation-list"),
    path("create/", views.conversation_create, name="conversation-create"),
    path("<int:pk>/", views.conversation_detail, name="conversation-detail"),
    path("<int:pk>/delete/", views.conversation_delete, name="conversation-delete"),
]