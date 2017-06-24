"""Contains form for bucket.
"""


from django.forms import ModelForm
from myrm_app.models import Bucket


class BucketForm(ModelForm):
    """Form for bucket.
    """
    class Meta():
        model = Bucket
        fields = ["name", "directory"]
