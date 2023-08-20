from django.contrib import admin

# Register your models here.
from faculty.models import Course,Semester,Subject



admin.site.register(Course)
admin.site.register(Semester)
admin.site.register(Subject)