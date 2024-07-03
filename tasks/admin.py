from django.contrib import admin
from .models import Task, Milestone


class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'due_date',
                    'project', 'assigned_to')
    search_fields = ('name', 'description')


class MilestoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'due_date', 'project')
    search_fields = ('name', 'description')


admin.site.register(Task, TaskAdmin)
admin.site.register(Milestone, MilestoneAdmin)
