from rest_framework import serializers
from userprofile.models import TeacherProfile, StudentProfile, AdminProfile
from faculty.models import Subject, Semester
from django.db import models
from django.core.exceptions import ValidationError
from usermanagement.models import User


class TeacherProfileSerializer(serializers.ModelSerializer):
    user=serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    semester = serializers.SerializerMethodField()
    subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all(), required=False)
    
    class Meta:
        model = TeacherProfile
        fields = '__all__'
    
    def get_semester(self, obj):
        return obj.semester.all()
    
    
    degree=serializers.CharField(max_length=100,required=False)
    position=serializers.CharField(max_length=30,required=False)
    emergency_contact_person=serializers.CharField(max_length=30,required=False)
    emergency_contact_number=serializers.CharField(max_length=13,required=False)


    # checks if user already has a Teacher Profile
    def validate(self, attrs):
        user = attrs["user"]
        existing_profiles = TeacherProfile.objects.filter(user=user)
        if existing_profiles.exists():
            raise ValidationError("User already has a Teacher profile")
        return attrs

    
    
class StudentProfileSerializer(serializers.ModelSerializer):
    user=serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = StudentProfile
        fields = '__all__'
    semester=serializers.PrimaryKeyRelatedField(queryset=Semester.objects.all())
    parents_name=serializers.CharField(max_length=50,required=False)
    parents_contact_number=serializers.CharField(max_length=13,required=False)
    
    
    
    def validate(self, attrs):
        user = attrs["user"]
        existing_profiles = StudentProfile.objects.filter(user=user)
        if existing_profiles.exists():
            raise ValidationError("User already has a Student profile")
        return attrs

    
    
    
class AdminProfileSerializer(serializers.ModelSerializer):
    user=serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = AdminProfile
        fields = '__all__'
    emergency_contact_person=serializers.CharField(max_length=13,required=False)
    emergency_contact_number=serializers.CharField(max_length=13,required=False)
    position=serializers.CharField(max_length=30,required=False)
    
    

    def validate(self, attrs):
        user = attrs["user"]
        existing_profiles = AdminProfile.objects.filter(user=user)
        if existing_profiles.exists():
            raise ValidationError("User already has an Admin profile")
        return attrs
