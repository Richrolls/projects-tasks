from django.contrib import admin

# Register your models here.
from .models import Project


@admin.register(Project)
class ProjectCategory(admin.ModelAdmin):
    list_display = (
        "name",
    )
