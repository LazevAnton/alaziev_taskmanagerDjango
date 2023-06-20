from django.urls import path

from TaskManagement.views import about_view, tasks_view, create_task_view, sign_up_view, sign_in_view, \
    logout_view, task_view, task_update, task_delete

app_name = 'TaskManagement'

urlpatterns = [
    path('', tasks_view, name='main_page'),
    path('about/', about_view, name='about_page'),
    path('tasks/', tasks_view, name='tasks_list'),
    path('create/', create_task_view, name='create_task'),
    path('sign-up/', sign_up_view, name='signup'),
    path('sign-in/', sign_in_view, name='signin'),
    path('logout/', logout_view, name='logout'),
    path('<uuid:uuid>/', task_view, name='task_detail'),
    path('<uuid:uuid>/update/', task_update, name='task_update'),
    path('<uuid:uuid>/delete/', task_delete, name='task_delete')

]
