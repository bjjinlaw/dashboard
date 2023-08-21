from django.urls import path
from usermanagement.views import (UserRegisterView,UserDetailUpdateDeleteView)


app_name="user"

urlpatterns = [
    path("register/",UserRegisterView.as_view(),name="register/"),
    path("update-delete-user/<int:pk>/",UserDetailUpdateDeleteView.as_view(),name="update-delete/"),
]
