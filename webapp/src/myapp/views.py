from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from myapp.serializers import UserSerializer
from myapp.tasks import download_cat

UserModel = get_user_model()


class UserRegistration(ModelViewSet):
    download_cat.delay()
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        download_cat.delay()
        print(111111111111111)
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

