from rest_framework import serializers
from .models import Events, Notice, LostAndFound, Scholarship

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = "__all__"


class LostAndFoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostAndFound
        fields = "__all__"


class ScholarshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scholarship
        fields = "__all__"
        
        
class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = "__all__"
