from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from .models import Task

# Create your views here.


@login_required
def create_task(request):
    if request.method == "POST":
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect("list_projects")
    else:
        task_form = TaskForm()
    context = {
        "task_form": task_form,
    }
    return render(request, "tasks/create.html", context)
