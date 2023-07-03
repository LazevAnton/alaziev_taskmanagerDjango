from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, Textarea, Select
from django import forms

from TaskManagement.models import TasksModel, UserModel


class CreateTaskForm(forms.ModelForm):
    reporter = forms.ModelChoiceField(
        queryset=UserModel.objects.all(),
        widget=Select(attrs={'class': 'form-control', 'placeholder': 'Select reporter'})
    )

    assignee = forms.ModelChoiceField(
        queryset=UserModel.objects.all(),
        widget=Select(attrs={'class': 'form-control', 'placeholder': 'Select assignee'}))

    class Meta:
        model = TasksModel
        fields = ['title', 'description', 'reporter', 'assignee']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Type title'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Type description'
            })
        }
