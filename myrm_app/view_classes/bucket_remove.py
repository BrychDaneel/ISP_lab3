from myrm_app.models import Bukkit
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404

def bucket_remove(request, *args, **kwargs):
    """
    """
    bucket = get_object_or_404(Bukkit, pk=kwargs['id'])
    bucket.delete()
    bucket.parametrs.delete()
    return redirect(reverse('bukkit_list'))
