"""Contains method, than remove bucket.

Methods:
 * bucket_remove
"""


from myrm_app.models import Bucket
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404


def bucket_remove(request, *args, **kwargs):
    """Removes bucket.
    """
    bucket = get_object_or_404(Bucket, pk=kwargs['id'])
    bucket.delete()
    bucket.parametrs.delete()
    return redirect(reverse('bucket_list'))
