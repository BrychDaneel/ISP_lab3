from django.views.generic import DetailView
from myrm_app.models import Bukkit

class BucketDetails(DetailView):
    template_name = "bukkit_details.html"
    context_object_name = 'bucket'
    model = Bukkit
    pk_url_kwarg = "id"
