from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, TemplateView, CreateView, DetailView, DeleteView, UpdateView
from TaskManagement.forms import CreateTaskForm, UserRegisterForm
from TaskManagement.models import TasksModel


@method_decorator(login_required(login_url='TaskManagement:signin'), name='dispatch')
class TasksView(ListView):
    template_name = 'tasks_list.html'
    queryset = TasksModel.objects.order_by('-created_at')
    context_object_name = 'tasks'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Tasks'
        return context


class AboutPageView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'About'
        return context


@method_decorator(login_required(login_url='TaskManagement:signin'), name='dispatch')
class CreateTaskView(CreateView):
    template_name = 'create_task.html'
    model = TasksModel
    form_class = CreateTaskForm
    success_url = reverse_lazy('TaskManagement:main_page')

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['title'] = 'CreateTask'
        return contex


class SignUpView(View):
    form_class = UserRegisterForm
    template_name = 'sign_up.html'
    success_url = 'TaskManagement:signin'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = {
            'title': 'Registration',
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect(self.success_url)
        context = {
            'title': 'Registration',
            'form': form
        }
        return render(request, self.template_name, context)


class TaskView(DetailView):
    template_name = 'task_details.html'
    model = TasksModel

    def get(self, request, uuid, *args, **kwargs):
        task = get_object_or_404(self.model, uuid=uuid)
        context = {
            'title': 'TaskView',
            'task': task
        }
        return render(request, self.template_name, context)


class LoginUserView(LoginView):
    template_name = 'sign_in.html'
    next_page = 'TaskManagement:tasks_list'


class LogOutUserView(LogoutView):
    next_page = 'TaskManagement:signin'


class TaskUpdateView(UpdateView):
    template_name = 'task_update.html'
    model = TasksModel
    form_class = CreateTaskForm

    def get_object(self, queryset=None):
        uuid = self.kwargs.get('uuid')
        return get_object_or_404(self.model, uuid=uuid)

    def form_valid(self, form):
        task = form.instance
        if task.reporter == self.request.user or task.assignee == self.request.user:
            if task.execution_status:
                messages.error(self.request, f'This task already completed')
                return self.form_invalid(form)
            else:
                return super().form_valid(form)
        else:
            messages.error(self.request, f'Only {task.reporter} or {task.assignee}'
                                         f'can update this task')
            return self.form_invalid(form)

    def get_success_url(self):
        uuid = self.kwargs.get('uuid')
        return reverse_lazy('TaskManagement:task_detail', kwargs={'uuid': uuid})


class TaskDeleteView(DeleteView):
    model = TasksModel
    template_name = 'task_delete.html'
    success_url = reverse_lazy('TaskManagement:main_page')

    def get_object(self, queryset=None):
        uuid = self.kwargs.get('uuid')
        return get_object_or_404(self.model, uuid=uuid)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.reporter != request.user:
            messages.error(request, f'Only {self.object.reporter} or {self.object.assignee} can delete this task')
            return redirect('TaskManagement:task_detail', uuid=self.object.uuid)
        elif self.object.execution_status:
            messages.error(request, 'You cannot delete a task with a "Completed" status')
            return redirect('TaskManagement:task_detail', uuid=self.object.uuid)
        else:
            self.object.delete()
            messages.success(request, 'Task deleted successfully')
            return redirect(self.success_url)
