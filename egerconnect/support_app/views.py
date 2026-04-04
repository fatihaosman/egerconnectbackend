# support/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SupportMessage

@api_view(['POST'])
def create_message(request):
    data = request.data
    message = SupportMessage.objects.create(
        name=data.get("name"),
        email=data.get("email"),
        subject=data.get("subject"),
        message=data.get("message"),
    )
    return Response({"success": True})