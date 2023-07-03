from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout

from TaskManagement.forms import CreateTaskForm
from TaskManagement.models import TasksModel


def tasks_view(request):
    tasks = TasksModel.objects.order_by('-created_at')
    contex = {
        'title': 'Main',
        'tasks': tasks
    }
    return render(request, 'tasks_list.html', contex)


def about_view(request):
    contex = {
        'title': 'About'
    }
    return render(request, 'about.html', contex)


def create_task_view(request):
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('TaskManagement:main_page')
    else:
        form = CreateTaskForm()

    contex = {
        'title': 'Create task',
        'form': form
    }
    return render(request, 'create_task.html', contex)


def sign_up_view(request):
    contex = {
        'title': 'SignUp',
    }
    return render(request, 'sign_up.html', contex)


def sign_in_view(request):
    contex = {
        'title': 'SignIn',
    }
    return render(request, 'sign_in.html', contex)


def logout_view(request):
    logout(request)
    contex = {
        'title': 'LogOut'
    }
    return render(request, 'logout.html', contex)


def task_view(request, uuid):
    task = get_object_or_404(TasksModel, uuid=uuid)
    context = {
        'title': 'TaskView',
        'task': task
    }
    return render(request, 'task_details.html', context)


def task_update(request, uuid):
    context = {
        'title': 'TaskUpdate'
    }
    return render(request, 'task_update.html', context)


def task_delete(request, uuid):
    context = {
        'title': 'TaskDelete'
    }
    return render(request, 'task_delete.html', context)
