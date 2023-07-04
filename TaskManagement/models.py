import uuid

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models


class TasksModel(models.Model):
    STATUS_CHOICES = [
        (False, 'Pending'),
        (True, 'Completed'),
    ]
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    execution_status = models.BooleanField(default=False, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reporter = models.ForeignKey("UserModel", on_delete=models.PROTECT, related_name='reporter_task')
    assignee = models.ForeignKey("UserModel", on_delete=models.PROTECT, related_name='assignee_task')

    def __str__(self):
        return f'{self.reporter} - {self.title}'


class UserModel(AbstractUser):
    username = models.CharField(max_length=32, unique=True)
    first_name = models.CharField(max_length=32, blank=True)
    last_name = models.CharField(max_length=32, blank=True)
    email = models.EmailField(max_length=64, unique=True)

    class Meta:
        db_table = "User_custom_auth"

    def __str__(self):
        return self.get_full_name() or self.username
