from rest_framework import viewsets
from .models import Events, Notice, LostAndFound, Scholarship, SupportRequest
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, permissions
from .serializers import (
    EventsSerializer,
    NoticeSerializer,
    LostAndFoundSerializer,
    SupportRequestSerializer,
    ScholarshipSerializer
)
from rest_framework.permissions import IsAdminUser, AllowAny
from django.shortcuts import render



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
    
    
# class SupportRequestViewSet(viewsets.ModelViewSet):
#     queryset = SupportRequest.objects.all()
#     serializer_class = SupportRequestSerializer

#     def get_permissions(self):
#         if self.action in ["list", "retrieve"]:
#             return [permissions.IsAdminUser()]  # Only admins can see all requests
#         return [permissions.IsAuthenticated()]  # Only logged-in users can create

#     def perform_create(self, serializer):
#         # Assign the logged-in user automatically when creating
#         serializer.save(user=self.request.user)
    
    
    
# class SupportRequestViewSet(viewsets.ModelViewSet):
#     queryset = SupportRequest.objects.all()
#     serializer_class = SupportRequestSerializer

#     def get_permissions(self):
#         if self.action in ["list", "retrieve"]:
#             return [permissions.IsAdminUser()]
#         return [permissions.AllowAny()]
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


class SupportRequestViewSet(viewsets.ModelViewSet):
    queryset = SupportRequest.objects.all()
    serializer_class = SupportRequestSerializer

    def get_permissions(self):
        # Admin can list and retrieve
        if self.action in ["list", "retrieve"]:
            return [permissions.IsAdminUser()]

        # Only authenticated users can create
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        # Admin sees all
        if self.request.user.is_staff:
            return SupportRequest.objects.all()

        # Students see only their own
        return SupportRequest.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Prevent admin from creating support request
        if self.request.user.is_staff:
            raise PermissionDenied("Admins cannot create support requests.")

        serializer.save(user=self.request.user)
        


# --- Template Views ---
def events_page(request):
    events = Events.objects.all().order_by("-created_at")
    return render(request, "posts/events.html", {"events": events})

def notices_page(request):
    notices = Notice.objects.all().order_by("-created_at")
    return render(request, "posts/notices.html", {"notices": notices})

def lost_and_found_page(request):
    items = LostAndFound.objects.all().order_by("-created_at")
    return render(request, "posts/lost_and_found.html", {"items": items})

def scholarships_page(request):
    scholarships = Scholarship.objects.all().order_by("-created_at")
    return render(request, "posts/scholarships.html", {"scholarships": scholarships})

def support_request_page(request):
    return render(request, "posts/support_request.html")