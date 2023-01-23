from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def projects_list(request):
    user = request.user
    projects_list = Project.objects.filter(owner=user)
    context = {
        "projects_list": projects_list,
    }
    return render(request, "projects/list.html", context)


@login_required
def show_project(request, id):
    show_project = get_object_or_404(Project, id=id)
    context = {
        "show_project": show_project,
    }
    return render(request, "projects/detail.html", context)


@login_required
def create_project(request):
    if request.method == "POST":
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            project_form.save()
            return redirect("list_projects")
    else:
        project_form = ProjectForm()
    context = {
        "project_form": project_form,
    }
    return render(request, "projects/create.html", context)
