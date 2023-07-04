from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_http_methods

from TaskManagement.forms import CreateTaskForm, UserRegisterForm, LoginUserForm
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


@require_http_methods(["GET", "POST"])
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


@require_http_methods(["GET", "POST"])
def sign_up_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('TaskManagement:signin')
    else:
        form = UserRegisterForm()
    contex = {
        'title': 'SignUp',
        'form': form
    }
    return render(request, 'sign_up.html', contex)


@require_http_methods(["GET", "POST"])
def sign_in_view(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('TaskManagement:tasks_list')
            else:
                form.add_error(None, 'Invalid username or password ')
    else:
        form = LoginUserForm()
    contex = {
        'title': 'SignIn',
        'form': form
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


@require_http_methods(["GET", "POST"])
def task_update(request, uuid):
    task = get_object_or_404(TasksModel, uuid=uuid)
    if request.method == 'POST':
        if task.reporter == request.user or task.assignee == request.user:
            if task.execution_status:
                messages.error(request, 'This task is already completed')
            else:
                form = CreateTaskForm(request.POST, instance=task)
                if form.is_valid():
                    form.save()
                    return redirect('TaskManagement:task_detail', uuid=uuid)
        else:
            messages.error(request, f'Only author {task.reporter} or {task.assignee} can update task')
    else:
        form = CreateTaskForm(instance=task)
        context = {
            'title': 'TaskUpdate',
            'form': form
        }
        return render(request, 'task_update.html', context)
    return redirect('TaskManagement:task_detail', uuid=uuid)


def task_delete(request, uuid):
    task = get_object_or_404(TasksModel, uuid=uuid)
    if task.reporter != request.user:
        messages.error(request, f'Only author {task.reporter} can delete this task')
    elif task.execution_status:
        messages.error(request, f'You cannot delete a task with a "Complete" status')
    else:
        task.delete()
        return redirect('TaskManagement:tasks_list')
    return redirect('TaskManagement:task_detail', uuid=uuid)
