from rest_framework import viewsets
from .models import Events, Notice, LostAndFound, Scholarship
from .serializers import (
    EventsSerializer,
    NoticeSerializer,
    LostAndFoundSerializer,
    ScholarshipSerializer
)
from rest_framework.permissions import IsAdminUser, AllowAny

class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all().order_by("-created_at")
    serializer_class = NoticeSerializer
    def get_permissions(self):
        if self.request.method in ["POST", "PUT", "PATCH", "DELETE"]:
            return [IsAdminUser()]
        return [AllowAny()]


class LostAndFoundViewSet(viewsets.ModelViewSet):
    queryset = LostAndFound.objects.all().order_by("-created_at")
    serializer_class = LostAndFoundSerializer
    def get_permissions(self):
        if self.request.method in ["POST", "PUT", "PATCH", "DELETE"]:
            return [IsAdminUser()]
        return [AllowAny()]


class ScholarshipViewSet(viewsets.ModelViewSet):
    queryset = Scholarship.objects.all().order_by("-created_at")
    serializer_class = ScholarshipSerializer
    def get_permissions(self):
        if self.request.method in ["POST", "PUT", "PATCH", "DELETE"]:
            return [IsAdminUser()]
        return [AllowAny()]
    
class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all().order_by("-created_at")
    serializer_class = EventsSerializer
    def get_permissions(self):
        if self.request.method in ["POST", "PUT", "PATCH", "DELETE"]:
            return [IsAdminUser()]
        return [AllowAny()]
