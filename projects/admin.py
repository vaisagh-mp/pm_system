from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'start_date', 'end_date')
    search_fields = ('name', 'description')


admin.site.register(Project, ProjectAdmin)
