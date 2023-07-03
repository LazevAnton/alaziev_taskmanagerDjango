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


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Repeat your password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginUserForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
