from django.shortcuts import render


def index_view(request):
    contex = {
        'title': 'Main'
    }
    return render(request, 'index.html', contex)


def about_view(request):
    contex = {
        'title': 'About'
    }
    return render(request, 'about.html', contex)


def tasks_view(request):
    contex = {
        'title': 'Tasks'
    }
    return render(request, 'tasks_list.html', contex)


def create_task_view(request):
    contex = {
        'title': 'Create task'
    }
    return render(request, 'create_task.html', contex)


def sign_up_view(request):
    contex = {
        'title': 'SignUp'
    }
    return render(request, 'sign_up.html', contex)


def sign_in_view(request):
    contex = {
        'title': 'SignIn'
    }
    return render(request, 'sign_in.html', contex)


def logout_view(request):
    contex = {
        'title': 'LogOut'
    }
    return render(request, 'logout.html', contex)


def task_view(request, uuid):
    context = {
        'title': 'TaskView'
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
