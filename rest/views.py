from rest_framework import generics
from TaskManagement.models import TasksModel, UserModel
from rest.serializers import TaskModelSerializer, UserModelSerializer


class TaskListCreateAPIView(generics.ListCreateAPIView):
    queryset = TasksModel.objects.all()
    serializer_class = TaskModelSerializer


class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TasksModel.objects.all()
    serializer_class = TaskModelSerializer
    lookup_field = 'uuid'


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
    lookup_field = 'id'
