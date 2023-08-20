from django.db import models

# Create your models here.



class BaseModel(models.Model):
    name=models.CharField(max_length=100)
    
    class Meta:
        abstract = True
    

class Course(BaseModel):
    credit_hour=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    


class Semester(BaseModel):
    course=models.ForeignKey(Course,on_delete=models.CASCADE,related_name="semester")
    
    def __str__(self):
        return self.name
    
    
    
class Subject(BaseModel):
    semester=models.ManyToManyField(Semester,related_name="subject")
    def __str__(self):
        return self.name
    

