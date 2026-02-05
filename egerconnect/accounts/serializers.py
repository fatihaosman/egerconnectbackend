from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "full_name",
            "registration_number",
            "email",
            "faculty_department",
            "phone_number",
            "password",
        ]

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create_user(
            password=password,
            **validated_data
        )
        return user
      
      

class LoginSerializer(serializers.Serializer):
    registration_number = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        registration_number = data.get("registration_number")
        password = data.get("password")

        if registration_number and password:
            user = authenticate(
                username=registration_number,  # matches USERNAME_FIELD
                password=password
            )
            if not user:
                raise serializers.ValidationError("Invalid credentials")
        else:
            raise serializers.ValidationError("Both fields are required")

        data["user"] = user
        return data

