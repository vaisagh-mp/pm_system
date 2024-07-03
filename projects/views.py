from rest_framework import generics
from .models import Project
from .serializers import ProjectSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from pm_system.utils.cache import cache_data, get_cached_data, delete_cached_data
from tasks.permissions import IsAdminOrReadOnly, IsManagerOrReadOnly


class ProjectListCreateView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        queryset = get_cached_data('projects')
        if not queryset:
            queryset = Project.objects.select_related('created_by').all()
            cache_data('projects', queryset)
        return queryset

    def perform_create(self, serializer):
        super().perform_create(serializer)
        delete_cached_data('projects')


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        return Project.objects.select_related('created_by').all()

    def perform_update(self, serializer):
        super().perform_update(serializer)
        delete_cached_data('projects')

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        delete_cached_data('projects')
