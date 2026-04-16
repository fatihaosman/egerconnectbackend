from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
import re
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  #writeonly-password will never be  included in response for security reasons

    class Meta:   #so we are working with user model and these are the fields we want to include in our serializer
        model = User
        fields = [
            "full_name",
            "registration_number",
            "email",
            "faculty_department",
            "phone_number",
            "password",
        ]
    #  Email validation to ensure it follows the format
    def validate_email(self, value):
        pattern = r"^[A-Z]+\.\d+@student\.egerton\.ac\.ke$"
        if not re.match(pattern, value):
            raise serializers.ValidationError(
                "Email must follow the format: LASTNAME.######@student.egerton.ac.ke"
            )
        if User.objects.filter(email=value).exists():
          raise serializers.ValidationError("Email already registered.")
        return value
    
    # Validates that the password is at least 8 characters long and contains uppercase, lowercase, and a number
    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")

        if not re.search(r"[A-Z]", value):
            raise serializers.ValidationError("Password must contain at least one uppercase letter.")

        if not re.search(r"[a-z]", value):
            raise serializers.ValidationError("Password must contain at least one lowercase letter.")

        if not re.search(r"[0-9]", value):
            raise serializers.ValidationError("Password must contain at least one number.")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
           raise serializers.ValidationError(
           "Password must contain at least one special character."
    )

        return value
    # Validates that the phone number starts with 07 and is 10 digits long
    def validate_phone_number(self, value):
        if not re.match(r"^07\d{8}$", value):
            raise serializers.ValidationError(
                "Phone number must start with 07 and be 10 digits."
            )
        if User.objects.filter(phone_number=value).exists():
         raise serializers.ValidationError("Phone number already exists.")
        return value
    
    
    def validate_registration_number(self, value):
        if User.objects.filter(registration_number=value).exists():
            raise serializers.ValidationError("Registration number already exists.")

        return value
        
    #  #  General validation (duplicate email)
    # def validate(self, data):
    #     if User.objects.filter(email=data.get("email")).exists():
    #         raise serializers.ValidationError({
    #             "email": "This email is already registered."
    #         })
    #     return data
    # remove password from validated data and create user using create_user method in user manager which handles password hashing and saving to db
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create_user(
            password=password,
            **validated_data
        )
        return user
      
      

class LoginSerializer(serializers.Serializer): #we are not using model here because we are just validating email and password and not creating any new user
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        user = authenticate(username=email, password=password)

        if not user:
            raise serializers.ValidationError("Invalid credentials")

        data["user"] = user
        return data
    
    
    # accounts/serializers.py


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['full_name'] = user.full_name
        token['email'] = user.email
        token['registration_number'] = user.registration_number
        token['is_staff'] = user.is_staff   
        token['is_superuser'] = user.is_superuser  

        return token


