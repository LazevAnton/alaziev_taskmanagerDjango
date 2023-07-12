from django.urls import path
from TaskManagement.views import AboutPageView, TasksView, CreateTaskView, \
    TaskUpdateView, TaskDeleteView, SignUpView, LoginUserView, LogOutUserView, TaskView

app_name = 'TaskManagement'

urlpatterns = [
    path('', TasksView.as_view(), name='main_page'),
    path('about/', AboutPageView.as_view(), name='about_page'),
    path('tasks/', TasksView.as_view(), name='tasks_list'),
    path('create/', CreateTaskView.as_view(), name='create_task'),
    path('sign-up/', SignUpView.as_view(), name='signup'),
    path('sign-in/', LoginUserView.as_view(), name='signin'),
    path('logout/', LogOutUserView.as_view(), name='logout'),
    path('<uuid:uuid>/', TaskView.as_view(), name='task_detail'),
    path('<uuid:uuid>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('<uuid:uuid>/delete/', TaskDeleteView.as_view(), name='task_delete')

]
