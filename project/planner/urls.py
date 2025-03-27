from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("project/", views.project, name="project"),
    path("project/task", views.task, name="task"),
    path("project/task/subtask", views.subtask, name="subtask"),
]
