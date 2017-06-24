"""Contains view, that shows list of tasks.

Classes:
 * TaskList
"""


from django.views.generic import ListView
from myrm_app.models import Task


class TaskList(ListView):
    """Shows tasks list.
    """
    template_name = "task_list.html"
    queryset = Task.objects.order_by('created').reverse()
