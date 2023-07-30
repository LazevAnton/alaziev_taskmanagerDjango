from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from TaskManagement.models import TasksModel, UserModel


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'username', 'email', 'password']


class TaskModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TasksModel
        fields = ['uuid', 'title', 'description', 'execution_status',
                  'created_at', 'updated_at', 'reporter', 'assignee']


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token
