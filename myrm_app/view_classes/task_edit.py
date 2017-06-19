from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from myrm_app.models import Task
from myrm_app.view_classes.forms.task import TaskForm 
from myrm_app.view_classes.forms.parametrs import ParametrsForm


class TaskEdit(TemplateView):
    """
    """
    
    template_name = 'task_edit.html'

    task_form = None
    parametrs_form = None
    success_url = reverse_lazy("task_list")
    
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['id'])
        parametrs = task.parametrs
        self.task_form = TaskForm(instance=task, prefix='task_form')
        self.parametrs_form = ParametrsForm(instance=parametrs, prefix='parametrs_form')
        return super(TaskEdit, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(TaskEdit, self).get_context_data(**kwargs)
        context['task_form'] = self.task_form
        context['parametrs_form'] = self.parametrs_form
        return context

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['id'])
        parametrs = task.parametrs
        self.task_form = TaskForm(request.POST, instance=task, prefix='task_form')
        self.parametrs_form = ParametrsForm(request.POST, instance=parametrs,  prefix='parametrs_form')
        if self.task_form.is_valid() and self.parametrs_form.is_valid():
            self.parametrs_form.save()
            self.task_form.save()
            return redirect(TaskEdit.success_url)
        else:
            return super(TaskEdit, self).get(request, *args, **kwargs)
