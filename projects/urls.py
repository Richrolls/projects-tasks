from django.urls import path
from .views import projects_list, show_project, create_project


urlpatterns = [
    path("", projects_list, name="list_projects"),
    path("<int:id>/", show_project, name="show_project"),
    path("create/", create_project, name="create_project"),
]
