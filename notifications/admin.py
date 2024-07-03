from django.contrib import admin
from .models import Notification


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('message', 'user', 'created_at')
    search_fields = ('message',)


admin.site.register(Notification, NotificationAdmin)
