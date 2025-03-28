from django.urls import path
from . import views



urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("<slug:project_name>", views.ProjectPageView.as_view(), name="project"),
    path("<slug:project_name>/<int:task_id>", views.TaskPageView.as_view(), name="task"),
    path("project/task/subtask", views.subtask, name="subtask"),
    # path('project/<int:project_id>/tasks/', ProjectTasksView.as_view(), name='project_t   asks'),
]
