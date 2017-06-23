from myrm_app.models import Bucket
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404

def bucket_remove(request, *args, **kwargs):
    """
    """
    bucket = get_object_or_404(Bucket, pk=kwargs['id'])
    bucket.delete()
    bucket.parametrs.delete()
    return redirect(reverse('bucket_list'))
