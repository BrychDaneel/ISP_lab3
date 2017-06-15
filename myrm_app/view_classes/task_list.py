from django.views.generic import ListView
from myrm_app.models import Task

class TaskList(ListView):
    template_name = "task_list.html"
    model = Task
