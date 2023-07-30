from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from TaskManagement.models import TasksModel, UserModel
from rest.serializers import TaskModelSerializer, UserModelSerializer, CustomTokenObtainPairSerializer


class CustomObtainPairVIew(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class TaskListCreateAPIView(generics.ListCreateAPIView):
    queryset = TasksModel.objects.all()
    serializer_class = TaskModelSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TasksModel.objects.all()
    serializer_class = TaskModelSerializer
    lookup_field = 'uuid'
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
    lookup_field = 'id'
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
