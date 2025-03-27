from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, "planner/homepage.html")

def project(request):
    return render(request, "planner/task_list.html")

def task(request):
    return render(request, "planner/subtask_list.html")

def subtask(request):
    return render(request, "planner/subtask_detail.html")