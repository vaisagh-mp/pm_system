from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Task, Milestone
from .serializers import TaskSerializer, MilestoneSerializer
from pm_system.utils.cache import cache_data, get_cached_data, delete_cached_data
from .permissions import IsAdminOrReadOnly, IsManagerOrReadOnly
from .tasks import send_task_notification, send_milestone_notification


class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsManagerOrReadOnly]

    def get_queryset(self):
        queryset = get_cached_data('tasks')
        if not queryset:
            queryset = Task.objects.select_related(
                'project', 'assigned_to').all()
            cache_data('tasks', queryset)
        return queryset

    def perform_create(self, serializer):
        instance = serializer.save()
        send_task_notification.delay(instance.assigned_to.email, instance.name)
        delete_cached_data('tasks')


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsManagerOrReadOnly]

    def get_queryset(self):
        return Task.objects.select_related('project', 'assigned_to').all()

    def perform_update(self, serializer):
        instance = serializer.save()
        send_task_notification.delay(instance.assigned_to.email, instance.name)
        delete_cached_data('tasks')

    def perform_destroy(self, instance):
        send_task_notification.delay(instance.assigned_to.email, instance.name)
        super().perform_destroy(instance)
        delete_cached_data('tasks')


class MilestoneListCreateView(generics.ListCreateAPIView):
    serializer_class = MilestoneSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsManagerOrReadOnly]

    def get_queryset(self):
        queryset = get_cached_data('milestones')
        if not queryset:
            queryset = Milestone.objects.select_related('project').all()
            cache_data('milestones', queryset)
        return queryset

    def perform_create(self, serializer):
        instance = serializer.save()
        send_milestone_notification.delay(
            instance.project.manager.email, instance.name)
        delete_cached_data('milestones')


class MilestoneDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MilestoneSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsManagerOrReadOnly]

    def get_queryset(self):
        return Milestone.objects.select_related('project').all()

    def perform_update(self, serializer):
        instance = serializer.save()
        send_milestone_notification.delay(
            instance.project.manager.email, instance.name)
        delete_cached_data('milestones')

    def perform_destroy(self, instance):
        send_milestone_notification.delay(
            instance.project.manager.email, instance.name)
        super().perform_destroy(instance)
        delete_cached_data('milestones')
