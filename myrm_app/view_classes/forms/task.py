"""Contains form for task.

Classes:
 * TaskForm
"""


from django.forms import ModelForm
from myrm_app.models import Task


class TaskForm(ModelForm):
    """Form for task.
    """
    class Meta():
        model = Task
        fields = ['bucket', 'target', 'command']
