from django.urls import path
from userprofile.views import (
    TeacherProfileRegisterView, TeacherProfileUpdateView, TeacherProfileDeleteView,
    StudentProfileRegisterView, StudentProfileUpdateView, StudentProfileDeleteView,
    AdminProfileRegisterView, AdminProfileUpdateView, AdminProfileDeleteView
)

app_name = "userprofile"

urlpatterns = [
    path("register-teacher/", TeacherProfileRegisterView.as_view(), name="register-teacher"),
    path("update-teacher/<int:pk>/", TeacherProfileUpdateView.as_view(), name="update-teacher"),
    path("delete-teacher/<int:pk>/", TeacherProfileDeleteView.as_view(), name="delete-teacher"),

    path("register-student/", StudentProfileRegisterView.as_view(), name="register-student"),
    path("update-student/<int:pk>/", StudentProfileUpdateView.as_view(), name="update-student"),
    path("delete-student/<int:pk>/", StudentProfileDeleteView.as_view(), name="delete-student"),

    path("register-admin/", AdminProfileRegisterView.as_view(), name="register-admin"),
    path("update-admin/<int:pk>/", AdminProfileUpdateView.as_view(), name="update-admin"),
    path("delete-admin/<int:pk>/", AdminProfileDeleteView.as_view(), name="delete-admin"),
]
