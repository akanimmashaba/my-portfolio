from django.contrib import admin
from .models import Project


# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'resume')
    list_filter = ('resume',)
    search_fields = ('title', 'description')

    fieldsets = (
        ('Project Details', {
            'fields': ('resume', 'title', 'description')
        }),
        ('Contribution', {
            'fields': ('contribution',)
        }),
        ('Links', {
            'fields': ('github', 'link')
        }),
        ('Image', {
            'fields': ('image',)
        }),
    )