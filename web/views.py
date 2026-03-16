from django.shortcuts import render

def login_page(request):
    return render(request, "login.html")

def tasks_page(request):
    return render(request, "tasks/tasks_list.html")