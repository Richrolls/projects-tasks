from django.shortcuts import render
from .models import Project
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def projects_list(request):
    user = request.user
    projects = Project.objects.filter(owner=user)
    context = {
        "projects_list": projects,
    }
    return render(request, "projects/list.html", context)
