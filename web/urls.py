from django.urls import path
from .views import login_page, tasks_page

urlpatterns = [
    path('', login_page, name='login_page'),
    path('tasks-ui/', tasks_page, name='tasks_page'),
]