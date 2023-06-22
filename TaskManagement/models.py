import uuid

from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


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
    reporter = models.ForeignKey(UserModel, on_delete=models.PROTECT, related_name='reporter_user')
    assignee = models.ForeignKey(UserModel, on_delete=models.PROTECT, related_name='assignee_user')

    def __str__(self):
        return f'{self.reporter} - {self.title}'
