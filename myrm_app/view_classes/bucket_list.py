"""Contains model, than shows list of buckets.

Classes:
 * BucketList
"""


from django.views.generic import ListView
from myrm_app.models import Bucket


class BucketList(ListView):
    """Shows list of buckets.
    """
    template_name = "bucket_list.html"
    model = Bucket
