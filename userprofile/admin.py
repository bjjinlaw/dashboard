from django.contrib import admin
# from userprofile.models import
from .models import StudentProfile,TeacherProfile,AdminProfile

# Register your models here.


admin.site.register(StudentProfile)
admin.site.register(TeacherProfile)
admin.site.register(AdminProfile)