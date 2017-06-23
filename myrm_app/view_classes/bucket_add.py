from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from myrm_app.models import Bucket
from myrm_app.view_classes.forms.bucket import BucketForm 
from myrm_app.view_classes.forms.parametrs import ParametrsForm


class BucketAdd(TemplateView):
    """
    """
    
    template_name = 'bucket_add.html'

    bucket_form = None
    parametrs_form = None
    success_url = reverse_lazy("bucket_list")
    
    def get(self, request, *args, **kwargs):
        self.bucket_form = BucketForm(prefix='bucket_form')
        self.parametrs_form = ParametrsForm(prefix='parametrs_form')
        return super(BucketAdd, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BucketAdd, self).get_context_data(**kwargs)
        context['bucket_form'] = self.bucket_form
        context['parametrs_form'] = self.parametrs_form
        return context

    def post(self, request, *args, **kwargs):
        self.bucket_form = BucketForm(request.POST, prefix='bucket_form')
        self.parametrs_form = ParametrsForm(request.POST, prefix='parametrs_form')
        if self.bucket_form.is_valid() and self.parametrs_form.is_valid():
            parametrs = self.parametrs_form.save()
            bucket = self.bucket_form.save(commit=False)
            bucket.parametrs = parametrs
            bucket.save()
            return redirect(BucketAdd.success_url)
        else:
            return super(BucketAdd, self).get(request, *args, **kwargs)
