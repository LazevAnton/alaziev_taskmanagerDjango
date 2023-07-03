from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from TaskManagement.forms import CreateTaskForm, RegisterUserForm, LoginUserForm
from TaskManagement.models import TasksModel


@login_required(login_url='TaskManagement:signin')
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
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('TaskManagement:signin')
    else:
        form = RegisterUserForm()
    contex = {
        'title': 'SignUp',
        'form': form
    }
    return render(request, 'sign_up.html', contex)


def sign_in_view(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None and user.check_password(password):
                login(request, user)
                return redirect('TaskManagement:main_page')
            else:
                form.add_error(None, 'Invalid username or password')
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
