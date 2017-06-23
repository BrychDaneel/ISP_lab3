from django.views.generic import ListView
from myrm_app.models import Bucket

class BucketList(ListView):
    template_name = "bucket_list.html"
    model = Bucket
