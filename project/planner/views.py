from django.shortcuts import render
from django.views.generic import TemplateView



# class HomePageView(TemplateView):
#     template_name = "planner/homepage.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # context["projects"] = ["popa"]
#       #  context["latest_articles"] = Project.objects.all()[:5]
#         return context

class Prj():
    name = "popa"

class HomePageView(TemplateView):
    template_name = "planner/homepage.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pr1 = Prj()
        pr2 = Prj()
        pr2.name = "popa2"
        context["projects"] = [pr1, pr2]
        return  context

def project(request):
    return render(request, "planner/task_list.html")

def task(request):
    return render(request, "planner/subtask_list.html")

def subtask(request):
    return render(request, "planner/subtask_detail.html")