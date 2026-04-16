# support/views.py

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import SupportMessage
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_message(request):
    user = request.user  # 🔥 THIS is the logged-in user

    message = SupportMessage.objects.create(
        name=user.full_name,   # ✅ from backend
        email=user.email,      # ✅ from backend
        subject=request.data.get("subject"),
        message=request.data.get("message"),
    )

    return Response({"success": True})