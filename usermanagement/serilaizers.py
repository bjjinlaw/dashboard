from usermanagement.models import User
from rest_framework import serializers
from userprofile.models import StudentProfile,TeacherProfile,AdminProfile





class UserRegisterSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=25)
    address=serializers.CharField(max_length=100)
    phone_number=serializers.CharField(max_length=10)
    user_type=serializers.CharField(max_length=10)
    dob=serializers.CharField(max_length=100)
    blood_group=serializers.CharField(max_length=10)
    marital_status=serializers.CharField(max_length=10)
    gender=serializers.CharField(max_length=10)
    email=serializers.EmailField()
    password1=serializers.CharField(min_length=8,max_length=20)
    password2=serializers.CharField(min_length=8,max_length=20)
    first_name=serializers.CharField(max_length=25)
    middle_name=serializers.CharField(max_length=25,required=False)
    last_name=serializers.CharField(max_length=25)
    

    
    
    def validate(self, attrs):
        password1=attrs["password1"]
        password2=attrs["password2"]
        if password1!=password2:
            raise serializers.ValidationError("Both Password Doesn't Match")
        return attrs
    
    
    
    def validate_email(self,value):
        active_user=User.objects.filter(email=value)
        if active_user:
            raise serializers.ValidationError("User With Such Credential Already Exists !!")
        return value
        
    def validate_username(self,value):
        active_user=User.objects.filter(username=value)
        if active_user:
            raise serializers.ValidationError("User With Such Credential Already Exists !!")
        return value
    
    
    def validate_user_type(self,value):
        if int(value)>3 and int(value)<1:
            raise serializers.ValidationError(" UserType Mismatched ")
        return value
    
    
    def create(self, validated_data):
        username=validated_data.get("username")
        password=validated_data.get("password1") 
        address=password=validated_data.get("password1") 
        phone_number=password=validated_data.get("password1") 
        user_type=validated_data.get("user_type") 
        dob=validated_data.get("dob") 
        blood_group=validated_data.get("blood_group") 
        marital_status=validated_data.get("marital_status") 
        gender=validated_data.get("gender") 
        email=validated_data.get("email") 
        first_name=validated_data.get("first_name") 
        middle_name=validated_data.get("middle_name") 
        last_name=validated_data.get("last_name") 
        user=User.objects.create_user(email=email,user_type=user_type,dob=dob,blood_group=blood_group,marital_status=marital_status, gender=gender,first_name=first_name,middle_name=middle_name,last_name=last_name,password=password,address=address,phone_number=phone_number,username=username)
        
        # checks if user has existing profile
        
        if int(user_type) == 1:
            existing_profiles = StudentProfile.objects.filter(user=user)
        elif int(user_type) == 2:
            existing_profiles = TeacherProfile.objects.filter(user=user)
        elif int(user_type) == 3:
            existing_profiles = AdminProfile.objects.filter(user=user)
        
        if existing_profiles and existing_profiles.exists():
            raise serializers.ValidationError("User already has a profile of the same type")
        
        # creates profile if validation passes
        
        if int(user_type)==1:
            StudentProfile.objects.create(user=user)
        elif int(user_type)==2:
            TeacherProfile.objects.create(user=user)
        elif int(user_type)==3:
            AdminProfile.objects.create(user=user)
        return user
        
        
        
class UserDetailUpdataSerializer(serializers.ModelSerializer):
    username=serializers.CharField()

    class Meta:
        model=User
        exclude=("last_login","is_superuser","is_staff","is_active","date_joined","groups","user_permissions")
        
        
        
        
        
        
        
        
        
        
        