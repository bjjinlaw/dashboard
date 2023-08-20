from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
# from datetime import timedelta
# from django.utils import timezone
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
import uuid

# Create your models here.


class UserType(models.TextChoices):
    '''
        THIS IS TO GIVE USER A CHOICE
    '''
    STUDENT=1
    TEACHER=2
    ADMIN=3
    
    

    
class BLOOD_GROUP(models.TextChoices):
    A_Positive = 1
    A_Negative = 2
    AB_Positive = 3
    AB_Negative = 4
    B_Positive = 5
    B_Negative = 6
    O_Positive = 7
    O_Negative = 8
    
    
class MARITAL_STATUS(models.TextChoices):
    Married = 1
    Single = 2
    Divorced = 3
    Separated = 4
    Widowed = 5
    


class GenderChoices(models.TextChoices):
    Male = 1
    Female = 2



class CustomUserManager(BaseUserManager):
    '''
        Custom Manager to Create User and SuperUser
    '''
    def create_user(self,email,password=None,**extra_fields):
        '''
            Create Normal Users
        '''
        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,password=None,**extra_fields):
        '''
            Create Super User
        '''
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True ")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        '''
            Super must have all properties of normal user
        '''
        return self.create_user(email,password,**extra_fields)
        






class User(AbstractUser):
    email=models.EmailField(unique=True)
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    objects=CustomUserManager()
    address=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=10)
    user_type=models.CharField(max_length=10,choices=UserType.choices)
    dob=models.CharField(max_length=100)
    image=models.ImageField(upload_to="users_profile",blank=True,null=True)
    blood_group=models.CharField(max_length=10,choices=BLOOD_GROUP.choices)
    marital_status=models.CharField(max_length=10,choices=MARITAL_STATUS.choices)
    gender=models.CharField(max_length=10,choices=GenderChoices.choices)
    middle_name=models.CharField(max_length=25,blank=True,null=True)
    
    
  
    class Meta:
        verbose_name='User'
        verbose_name_plural="Users"
        
        


    
    
    
    
    

    
    

    

