from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Task, Milestone
from notifications.models import Notification


@receiver(post_save, sender=Task)
def create_task_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.assigned_to,
            message=f'A new task "{instance.name}" has been assigned to you.'
        )
    else:
        Notification.objects.create(
            user=instance.assigned_to,
            message=f'The task "{instance.name}" has been updated.'
        )


@receiver(post_save, sender=Milestone)
def create_milestone_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.project.created_by,
            message=f'A new milestone "{instance.name}" has been created for the project "{instance.project.name}".'
        )
    else:
        Notification.objects.create(
            user=instance.project.created_by,
            message=f'The milestone "{instance.name}" has been updated.'
        )
