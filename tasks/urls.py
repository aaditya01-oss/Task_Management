from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, task_dashboard, task_create, task_delete

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    # API
    path("", include(router.urls)),

    # Web
    path("dashboard/", task_dashboard, name="task-dashboard"),
    path("create/", task_create, name="task-create"),
    path("delete/<int:pk>/", task_delete, name="task-delete"),
]