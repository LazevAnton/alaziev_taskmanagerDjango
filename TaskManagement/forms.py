from django.forms import TextInput, Textarea, Select, CheckboxInput
from django import forms
from TaskManagement.models import TasksModel, UserModel


class CreateTaskForm(forms.ModelForm):
    reporter = forms.ModelChoiceField(
        queryset=UserModel.objects.all(),
        widget=Select(attrs={'class': 'form-control'})
    )
    assignee = forms.ModelChoiceField(
        queryset=UserModel.objects.all(),
        widget=Select(attrs={'class': 'form-control'})
    )

    execution_status = forms.BooleanField(
        required=False,
        label='Complete task',
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        })
    )

    class Meta:
        model = TasksModel
        fields = ['title', 'description', 'reporter', 'assignee', 'execution_status']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Type title'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Type description'
            }),
        }


class UserRegisterForm(forms.ModelForm):
    confirm_password = forms.CharField()

    class Meta:
        model = UserModel
        fields = [
            'username', 'first_name',
            'last_name', 'email',
            'password'
        ]
        widgets = {
            'password': forms.PasswordInput,
            'confirm_password': forms.PasswordInput
        }

    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if UserModel.objects.filter(username=username).exists():
            raise forms.ValidationError(f'{username} already registered')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if UserModel.objects.filter(email=email).exists():
            raise forms.ValidationError(f'Email {email} already registered')
        return email


class LoginUserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = [
            'username',
            'password'
        ]
        widgets = {
            'password': forms.PasswordInput
        }
