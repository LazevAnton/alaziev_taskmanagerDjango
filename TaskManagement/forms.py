from django.core.exceptions import ValidationError
from django.forms import TextInput, Textarea, Select, CheckboxInput
from django import forms
from TaskManagement.models import TasksModel, UserModel


class CreateTaskForm(forms.ModelForm):
    reporter = forms.ModelChoiceField(
        queryset=UserModel.objects.all(),
        widget=Select(attrs={'class': 'form-control', 'placeholder': 'Select reporter'})
    )
    assignee = forms.ModelChoiceField(
        queryset=UserModel.objects.all(),
        widget=Select(attrs={'class': 'form-control', 'placeholder': 'Select assignee'})
    )
    execution_status = forms.ChoiceField(
        choices=TasksModel.STATUS_CHOICES,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        required=False,
        label='Complete task'
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


class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=32)
    first_name = forms.CharField(max_length=32, required=False)
    last_name = forms.CharField(max_length=32, required=False)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            UserModel.objects.get(username=username)
            raise ValidationError(f'{username}, already registered')
        except UserModel.DoesNotExist:
            return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            UserModel.objects.get(email=email)
            raise ValidationError(f'{email}, already registered')
        except UserModel.DoesNotExist:
            return email

    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', 'Passwords dont match')

    def save(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        email = self.cleaned_data['email']
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        user = UserModel.objects.create_user(username=username, password=password, email=email,
                                             first_name=first_name, last_name=last_name)
        return user


class LoginUserForm(forms.Form):
    username = forms.CharField(max_length=32)
    password = forms.CharField(widget=forms.PasswordInput)
