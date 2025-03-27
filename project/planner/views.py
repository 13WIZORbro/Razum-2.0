from django.shortcuts import render
from django.views.generic import TemplateView

from project.planner.models import Project


class HomePageView(TemplateView):
    template_name = "homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = Project.objects.f

def project(request):
    return render(request, "planner/task_list.html")

def task(request):
    return render(request, "planner/subtask_list.html")

def subtask(request):
    return render(request, "planner/subtask_detail.html")