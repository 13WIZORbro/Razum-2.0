from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, "planner/homepage.html")


def project(request):
    return render(request, "planner/project_homepage.html")
