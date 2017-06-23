from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from myrm_app.models import Bucket
from myrm_app.models import Task
from myrm_app.view_classes.forms.task import TaskForm 
from myrm_app.view_classes.forms.parametrs import ParametrsForm
from myrm_app.processor import start_process


class TaskAdd(TemplateView):
    """
    """
    
    template_name = 'task_add.html'

    task_form = None
    parametrs_form = None
    success_url = reverse_lazy("task_list")
    
    def get(self, request, *args, **kwargs):
        form_data = {}
        if 'target' in request.GET:
            form_data['target'] = request.GET['target']
        if 'command' in request.GET:
            form_data['command'] = request.GET['command']
        if 'bucket' in request.GET:
            bucket_id = request.GET['bucket']
            form_data['bucket'] = get_object_or_404(Bucket, pk=bucket_id)
        self.task_form = TaskForm(initial=form_data, prefix='task_form')
        
        bucket = form_data['bucket']
        if bucket:
            self.parametrs_form = ParametrsForm(prefix='parametrs_form', 
                                                initial=bucket.parametrs)
        return super(TaskAdd, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(TaskAdd, self).get_context_data(**kwargs)
        context['task_form'] = self.task_form
        context['parametrs_form'] = self.parametrs_form
        return context

    def post(self, request, *args, **kwargs):
        self.task_form = TaskForm(request.POST, prefix='task_form')
        self.parametrs_form = ParametrsForm(request.POST, prefix='parametrs_form')
        if self.task_form.is_valid() and self.parametrs_form.is_valid():
            parametrs = self.parametrs_form.save()
            task = self.task_form.save(commit=False)
            task.parametrs = parametrs
            task.save()
            start_process()
            return redirect(TaskAdd.success_url)
        else:
            return super(TaskAdd, self).get(request, *args, **kwargs)
