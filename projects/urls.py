from django.urls import path
from .views import projects_list, show_project


urlpatterns = [
    path("", projects_list, name="list_projects"),
    path("<int:id>/", show_project, name="show_project"),
]
