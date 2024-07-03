from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Notification
from .serializers import NotificationSerializer
from tasks.permissions import IsAdminOrReadOnly, IsManagerOrReadOnly


class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)


class NotificationUpdateView(generics.UpdateAPIView):
    serializer_class = NotificationSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)
