from django.urls import path
from .views import task_dashboard

urlpatterns = [
    path("", task_dashboard, name="task-dashboard"),
]