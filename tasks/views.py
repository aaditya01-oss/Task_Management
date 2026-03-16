from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import TaskForm 


@login_required
def task_dashboard(request):
    tasks = Task.objects.filter(owner=request.user).order_by("-created_at")
    return render(request, "tasks/tasks_list.html", {"tasks": tasks})

@login_required
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            return redirect("task-dashboard")
    else:
        form = TaskForm()

    return render(request, "tasks/tasks_form.html", {"form": form})