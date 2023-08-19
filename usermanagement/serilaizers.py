from usermanagement.models import User
from rest_framework import serializers





class UserRegisterSerializer(serializers.Serializer):
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
            raise serializers.ValidationError("User With Such Credential Already Exits !!")
        return value
        
        
    
    
    
    
    def create(self, validated_data): 
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
        # print(validated_data)
        return User.objects.create_user(email=email,user_type=user_type,dob=dob,blood_group=blood_group,marital_status=marital_status,     gender=gender,first_name=first_name,middle_name=middle_name,last_name=last_name,
                                 password=password,address=address,
                                 phone_number=phone_number)
        
        
        
    def update(self, instance, validated_data):
        # instance.name=validated_data.get('',instance.name)
        instance.email=validated_data.get("email",instance.email)
        instance.phone_number=validated_data.get("phone_number",instance.phone_number)
        instance.address=validated_data.get("address",instance.address)
        instance.user_type=validated_data.get("user_type",instance.user_type)
        instance.dob=validated_data.get("dob",instance.dob)
        instance.blood_group=validated_data.get("blood_group",instance.blood_group)
        instance.marital_status=validated_data.get("marital_status",instance.marital_status)
        instance.gender=validated_data.get("gender",instance.gender)
        instance.email=validated_data.get("email",instance.email)
        instance.password1=validated_data.get("password1",instance.password1)
        instance.first_name=validated_data.get("first_name",instance.first_name)
        instance.middle_name=validated_data.get("middle_name",instance.middle_name)
        instance.last_name=validated_data.get("last_name",instance.last_name)
        instance.save()
        return instance
        
        
        
       

    
    
    

    
    
    

