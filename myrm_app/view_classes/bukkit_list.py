from django.views.generic import ListView
from myrm_app.models import Task

class BukkitList(ListView):
    template_name = "task_list.html"
    model = Task