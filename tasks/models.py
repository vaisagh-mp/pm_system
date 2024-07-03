from django.db import models
from projects.models import Project
from users.models import User


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ForeignKey(
        Project, related_name='tasks', on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(
        User, related_name='tasks', on_delete=models.CASCADE, null=True, blank=True)
    due_date = models.DateField()

    def __str__(self):
        return self.name


class Milestone(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ForeignKey(
        Project, related_name='milestones', on_delete=models.CASCADE)
    due_date = models.DateField()

    def __str__(self):
        return self.name
