from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from .serializers import LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken



class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Student registered successfully"},
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            return Response(
                {
                    "message": "Login successful",
                    "registration_number": user.registration_number,
                    "full_name": user.full_name,
                    "email": user.email
                },
                status=200
            )
        return Response(serializer.errors, status=400)
    
        
        


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import LoginSerializer
# from rest_framework_simplejwt.tokens import RefreshToken
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import ensure_csrf_cookie

# @method_decorator(ensure_csrf_cookie, name="dispatch")
# class LoginView(APIView):
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.validated_data["user"]

#             # Create JWT token
#             refresh = RefreshToken.for_user(user)
#             access_token = str(refresh.access_token)

#             # Set cookie
#             response = Response(
#                 {
#                     "message": "Login successful",
#                     "registration_number": user.registration_number,
#                     "full_name": user.full_name,
#                     "email": user.email,
#                 },
#                 status=status.HTTP_200_OK,
#             )

#             # HttpOnly cookie
#             response.set_cookie(
#                 key="access_token",
#                 value=access_token,
#                 httponly=True,
#                 samesite="Lax",  # works with Next.js dev server
#                 secure=False,    # True if using HTTPS in production
#             )

#             return response

#         return Response(serializer.errors, status=400)
