from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from .models import Project, Task, Subtask


@method_decorator(login_required, name="dispatch")
class HomePageView(TemplateView):
    template_name = "planner/homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        user = self.request.user

        projects = Project.objects.filter(
            Q(manager=user) | Q(leader=user) | Q(tasks__performers=user)
        ).distinct()

        context["projects"] = projects
        return  context

class ProjectPageView(TemplateView):
    template_name = "planner/task_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        project_name = self.kwargs["project_name"]
        user = self.request.user


        projects = Project.objects.filter(
            Q(manager=user) | Q(leader=user) | Q(tasks__performers=user)
        ).distinct()

        current_project = get_object_or_404(Project, name=project_name)

        if current_project not in projects:
            raise PermissionDenied("У вас нет доступа к этому проекту")

        # tsk = Task(project=current_project, performers=(user))
        # tsk.save()


        # projects = projects + Task.objects().filter(project=current_project)

        tasks = Task.objects.filter(project=current_project)

        # performers = []
        # performers = [performers + i.objects.filte(performers=current_user) for i in tasks]
        # print(performers)

        print(tasks.all().values_list("performers"))

        context["tasks"] = tasks
        context["projects"] = projects
        context["current_project"] = current_project
        return  context

class TaskPageView(TemplateView):
    template_name = "planner/subtask_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        project_name = self.kwargs['project_name']
        task_id = self.kwargs["task_id"]
        user = self.request.user

        projects = Project.objects.filter(
            Q(manager=user) | Q(leader=user) | Q(tasks__performers=user)
        ).distinct()

        current_project = get_object_or_404(Project, name=project_name)
        current_task = get_object_or_404(Task, id=task_id)

        tasks = Task.objects.filter(project=current_project)

        subtasks = Subtask.objects.filter(task=current_task)

        context["subtasks"] = subtasks
        context["tasks"] = tasks
        context["projects"] = projects
        context["current_project"] = current_project
        context["current_task"] = current_task

        return context

def project(request):
    return render(request, "planner/project.html")

def task(request):
    return render(request, "planner/subtask_list.html")

def subtask(request):
    return render(request, "planner/subtask_detail.html")