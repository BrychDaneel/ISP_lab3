"""Contains view, than shows list of buckets.
"""


from django.views.generic import DetailView
from myrm_app.models import Bucket


class BucketDetails(DetailView):
    """Shows list of buckets.
    """
    template_name = "bucket_details.html"
    context_object_name = 'bucket'
    model = Bucket
    pk_url_kwarg = "id"
