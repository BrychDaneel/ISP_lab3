from django.views.generic import DetailView
from myrm_app.models import Task

class TaskDetails(DetailView):
    template_name = "task_details.html"
    context_object_name = 'task'
    model = Task
    pk_url_kwarg = "id"
