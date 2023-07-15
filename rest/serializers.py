from rest_framework import serializers
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
