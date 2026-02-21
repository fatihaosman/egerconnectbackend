from django.shortcuts import render
from rest_framework.views import APIView  #apiview allows me to handle http methods,get,put, return json respones and use serializers easily
from rest_framework.response import Response  #converts python dictionary into http responses, handles content type, works with status code
from rest_framework import status #more readble
from .serializers import RegisterSerializer, LoginSerializer   #view doesnt validate data it sends to serializers


class RegisterView(APIView):
    def post(self, request):  #this method runs when a post request is sent to this endpoint(which is registering/signup).....api/auth/register/..... request conatins data and user that is making the request
        serializer = RegisterSerializer(data=request.data)   #take incoming data and pass tto this serializer for validation and saving to db

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User registered successfully"},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  #400-invalid input

class LoginView(APIView):
    def post(self, request):   #runs when user is login in and sends post request to api/auth/login/ endpoint
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data["user"]

            return Response(
                {
                    "message": "Login successful",
                    "user": {
                        "id": user.id,
                        "email": user.email,
                        "full_name": user.full_name,
                        "registration_number": user.registration_number,
                    }
                },
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# --- Template Views ---
def register_page(request):
    return render(request, "accounts/register.html")

def login_page(request):
    return render(request, "accounts/login.html")