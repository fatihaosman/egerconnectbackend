from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
import re


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  #writeonly-password will never be  included in response for security reasons

    class Meta:   #sowe are working with user model and these are the fields we want to include in our serializer
        model = User
        fields = [
            "full_name",
            "registration_number",
            "email",
            "faculty_department",
            "phone_number",
            "password",
        ]
    def validate_email(self, value):
        pattern = r"^[A-Z]+\.\d+@student\.egerton\.ac\.ke$"
        if not re.match(pattern, value):
            raise serializers.ValidationError(
                "Email must follow the format: LASTNAME.######@student.egerton.ac.ke"
            )
        return value

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


