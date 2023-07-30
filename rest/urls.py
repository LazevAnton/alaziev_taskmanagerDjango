from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from rest.views import TaskListCreateAPIView, TaskRetrieveUpdateDestroyAPIView, UserListCreateAPIView, \
    UserRetrieveUpdateDestroyAPIView, CustomObtainPairVIew

urlpatterns = [
    path('token/', CustomObtainPairVIew.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh_token'),
    path('tasks/', TaskListCreateAPIView.as_view(), name='TasksList_CreateTask'),
    path('tasks/<uuid:uuid>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='TaskUpdateDestroy'),
    path('users/', UserListCreateAPIView.as_view(), name='CreateUser'),
    path('users/<int:id>', UserRetrieveUpdateDestroyAPIView.as_view(), name='UserUpdateDestroy')

]
