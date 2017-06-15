from django.forms import ModelForm
from myrm_app.models import Task


class TaskForm(ModelForm):
    class Meta():
        model = Task
        fields = ['bukkit', 'target', 'command']
