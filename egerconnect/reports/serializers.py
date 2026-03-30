from rest_framework import serializers
from posts.models import SupportRequest
from django.contrib.auth import get_user_model

from posts.models import Notice, Events, LostAndFound, Scholarship

class SupportRequestReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportRequest
        fields = ['id', 'request_type', 'status', 'created_at']
    # users/serializers.py



User = get_user_model()

class UserReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'date_joined']
        


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ['id', 'title', 'description', 'created_at']

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['id', 'title', 'description', 'created_at']

class LostAndFoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostAndFound
        fields = ['id', 'title', 'description', 'created_at']

class ScholarshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scholarship
        fields = ['id', 'title', 'description', 'created_at']