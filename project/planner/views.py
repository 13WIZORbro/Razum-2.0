from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Project




class HomePageView(TemplateView):
    # User = get_user_model()
    # user = User.objects.get(id=1)
    #print(" id = ", user.id)
    # pr = Project(name="test_name", manager=user, leader=user)
    # pr.save()

    template_name = "planner/homepage.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #print(Project.objects.all())
        context["projects"] = Project.objects.all()
        return  context

def project(request):
    return render(request, "planner/.html")

def task(request):
    return render(request, "planner/subtask_list.html")

def subtask(request):
    return render(request, "planner/subtask_detail.html")