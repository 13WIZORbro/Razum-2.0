from django.db import models
from django.contrib.auth import  get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

class BaseTask(models.Model):
    STATUS_CHOICES = [
        (1, 'New'),
        (2, 'In Progress'),
        (3, 'Completed'),
    ]
    name = models.CharField(max_length=200)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    class Meta:
        abstract = True



class Project(BaseTask):
    manager = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="projects")

    def __str__(self):
        return (f"Project: {self.name}\n"
                f"Manager: {self.manager}\n"
                f"Status: {self.status}\n"
                f"Deadline: {self.end_date}")



class Task(BaseTask):
    priority = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    performers = models.ManyToManyField(get_user_model(), related_name="assigned_tasks")
    additional_description = models.CharField(max_length=500)

    def __str__(self):
        return (f"Task: {self.name}\n"
                f"Status: {self.status}\n"
                f"Deadline: {self.end_date}\n"
                f"description: {self.additional_description}")



class Subtask(BaseTask):
    priority = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="subtasks")
    performer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="subtasks")
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="subtasks")
    additional_description = models.CharField(max_length=500)

    def __str__(self):
        return (f"Subtask: {self.name}\n"
                f"Status: {self.status}\n"
                f"Deadline: {self.end_date}\n"
                f"description: {self.additional_description}")



