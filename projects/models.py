from django.db import models
from users.models import User


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_by = models.ForeignKey(
        User, related_name='projects', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
