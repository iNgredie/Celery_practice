from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

from myapp.serializers import UserSerializer

UserModel = get_user_model()


class UserRegistration(ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
