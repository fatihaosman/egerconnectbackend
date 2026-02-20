from rest_framework import viewsets
from .models import Events, Notice, LostAndFound, Scholarship, SupportRequest
from rest_framework import generics, permissions
from .serializers import (
    EventsSerializer,
    NoticeSerializer,
    LostAndFoundSerializer,
    SupportRequestSerializer,
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
    
from rest_framework import viewsets, permissions
from .models import SupportRequest
from .serializers import SupportRequestSerializer


class SupportRequestViewSet(viewsets.ModelViewSet):
    queryset = SupportRequest.objects.all()
    serializer_class = SupportRequestSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve", "update", "destroy"]:
            return [permissions.IsAdminUser()]

        if self.action == "create":
            return [permissions.IsAuthenticated()]

        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    
# class SupportRequestViewSet(viewsets.ModelViewSet):
#     queryset = SupportRequest.objects.all()
#     serializer_class = SupportRequestSerializer

#     def get_permissions(self):
#         if self.action in ["list", "retrieve"]:
#             return [permissions.IsAdminUser()]
#         return [permissions.AllowAny()]

