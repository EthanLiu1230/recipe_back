from rest_framework import generics

from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """API View: Create a new user."""
    serializer_class = UserSerializer
