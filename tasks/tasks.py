from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task(bind=True)
def send_task_notification(self, email, task_name):
    send_mail(
        subject='New Task Assigned',
        message=f'You have been assigned a new task: {task_name}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=False,
    )


@shared_task(bind=True)
def send_milestone_notification(self, email, milestone_name):
    send_mail(
        subject='New Milestone Created/Updated',
        message=f'A new milestone has been created/updated: {milestone_name}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=False,
    )