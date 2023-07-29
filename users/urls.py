from django.urls import path

from lms_platform.views import UserCreateApiView
from users.apps import UsersConfig

app_name = UsersConfig.name
urlpatterns = [
    path('create/', UserCreateApiView.as_view()),
]
