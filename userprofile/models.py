from django.db import models
from faculty.models import Semester,Subject
from django.conf import settings

# Create your models here.

class TimestapModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateField(auto_now=True)
    class Meta:
        abstract=True
        
        
        
class StudentProfile(TimestapModel):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="studentprofile",unique=True)
    semester=models.OneToOneField(Semester,on_delete=models.SET_NULL,null=True,blank=True)
    parents_name=models.CharField(max_length=50,blank=True,null=True)
    parents_contact_number=models.CharField(max_length=13,blank=True,null=True)
    
    def __str__(self):
        return self.user.username
    
    
        
        
        
    
    
    
class TeacherProfile(TimestapModel):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="teacher_profile",unique=True)
    semester=models.ManyToManyField(Semester,related_name="teacher_semester")
    subject=models.ForeignKey(Subject,on_delete=models.SET_NULL,null=True,blank=True)
    degree=models.CharField(max_length=100,blank=True,null=True)
    position=models.CharField(max_length=30,blank=True,null=True)
    emergency_contact_person=models.CharField(max_length=30,blank=True,null=True)
    emergency_contact_number=models.CharField(max_length=13,blank=True,null=True)
    
    
    def __str__(self):
        return self.user.username
    

