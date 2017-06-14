from django.forms import ModelForm
from myrm_app.models import Bukkit


class BucketForm(ModelForm):
    class Meta():
        model = Bukkit
        fields = ["name", "directory"]
