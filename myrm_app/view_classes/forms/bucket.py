from django.forms import ModelForm
from myrm_app.models import Bucket


class BucketForm(ModelForm):
    class Meta():
        model = Bucket
        fields = ["name", "directory"]
