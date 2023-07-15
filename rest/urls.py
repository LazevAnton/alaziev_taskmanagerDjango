from django.urls import path

from rest.views import TaskListCreateAPIView, TaskRetrieveUpdateDestroyAPIView, UserListCreateAPIView, \
    UserRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('tasks/', TaskListCreateAPIView.as_view(), name='TasksList_CreateTask'),
    path('tasks/<uuid:uuid>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='TaskUpdateDestroy'),
    path('users/', UserListCreateAPIView.as_view(), name='CreateUser'),
    path('users/<int:id>', UserRetrieveUpdateDestroyAPIView.as_view(), name='UserUpdateDestroy')

]
