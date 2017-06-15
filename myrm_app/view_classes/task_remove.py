from myrm_app.models import Task
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404

def task_remove(request, *args, **kwargs):
    """
    """
    task = get_object_or_404(Task, pk=kwargs['id'])
    task.delete()
    task.parametrs.delete()
    return redirect(reverse('task_list'))
