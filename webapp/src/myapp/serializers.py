from django.contrib.auth.models import Group
from rest_framework import serializers
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)
        extra_kwargs = {
            'name': {'validators': []},
        }


class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        groups_data = validated_data.pop('groups')
        user = UserModel.objects.create(**validated_data)
        for group_data in groups_data:
            group = Group.objects.get(**group_data)
            user.groups.add(group)
        return user

    class Meta:
        model = UserModel

        fields = ("id", "email", "password", 'groups')
