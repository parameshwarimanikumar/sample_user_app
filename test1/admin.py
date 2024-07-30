from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'status', 'user', 'created_at', 'updated_at')
    search_fields = ('name',)

admin.site.register(Project, ProjectAdmin)
