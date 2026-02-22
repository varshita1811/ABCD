from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from elevate.models import User


class SignupView(APIView):

    def post(self, request):
        user_login = request.data.get("user_login")
        user_firstname = request.data.get("user_firstname")
        user_lastname = request.data.get("user_lastname")
        password = request.data.get("password")
        user_role = request.data.get("user_role")

        if not user_login or not password:
            return Response(
                {"error": "user login and password required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if User.objects.filter(user_login=user_login).exists():
            return Response(
                {"error": "User already exists"},
                status=status.HTTP_409_CONFLICT
            )

        user = User.objects.create_user(
            user_login=user_login,
            user_firstname=user_firstname,
            user_lastname=user_lastname,
            password=password,
            user_role=user_role
        )


        return Response(
            {"message": "User created successfully"},
            status=status.HTTP_201_CREATED
        )
    


class LoginView(APIView):

    def post(self, request):
        user_login = request.data.get("user_login")
        password = request.data.get("password")

        user = authenticate(
            request,
            user_login=user_login,
            password=password
        )

        if user is None:
            return Response(
                {"error": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user)

        return Response({
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
            "user": {
                "user_id": user.user_id,
                "user_login": user.user_login
            }
        })
    
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get("refresh_token")

        token = RefreshToken(refresh_token)
        token.blacklist()

        return Response(
            {"message": "Logged out successfully"},
            status=status.HTTP_205_RESET_CONTENT
        )