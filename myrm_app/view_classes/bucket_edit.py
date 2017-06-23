from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from myrm_app.models import Bucket
from myrm_app.view_classes.forms.bucket import BucketForm 
from myrm_app.view_classes.forms.parametrs import ParametrsForm


class BucketEdit(TemplateView):
    """
    """
    
    template_name = 'bucket_edit.html'

    bucket_form = None
    parametrs_form = None
    success_url = reverse_lazy("bucket_list")
    
    def get(self, request, *args, **kwargs):
        bucket = get_object_or_404(Bucket, pk=kwargs['id'])
        parametrs = bucket.parametrs
        self.bucket_form = BucketForm(instance=bucket, prefix='bucket_form')
        self.parametrs_form = ParametrsForm(instance=parametrs, prefix='parametrs_form')
        return super(BucketEdit, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BucketEdit, self).get_context_data(**kwargs)
        context['bucket_form'] = self.bucket_form
        context['parametrs_form'] = self.parametrs_form
        return context

    def post(self, request, *args, **kwargs):
        bucket = get_object_or_404(Bucket, pk=kwargs['id'])
        parametrs = bucket.parametrs
        self.bucket_form = BucketForm(request.POST, instance=bucket, prefix='bucket_form')
        self.parametrs_form = ParametrsForm(request.POST, instance=parametrs,  prefix='parametrs_form')
        if self.bucket_form.is_valid() and self.parametrs_form.is_valid():
            self.parametrs_form.save()
            self.bucket_form.save()
            return redirect(BucketEdit.success_url)
        else:
            return super(BucketEdit, self).get(request, *args, **kwargs)
