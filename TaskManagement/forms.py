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
    #
    # def clean_password(self):
    #     password = self.cleaned_data['password']
    #     confirm_password = self.cleaned_data.get('confirm_password')
    #     if password != confirm_password:
    #         self.add_error('confirm_password', 'Passwords do not match')
    #     return confirm_password

    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            self.add_error('confirm_password', 'Passwords do not match')


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
