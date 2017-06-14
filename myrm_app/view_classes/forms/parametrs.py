from django.forms import ModelForm
from myrm_app.models import Parametrs


class ParametrsForm(ModelForm):
    class Meta():
        model = Parametrs
        fields = ['force', 'dryrun', 'auto_replace', 'allow_autoclean',
                  'trash_max_size', 'trash_max_count',
                   'autoclean_count', 'autoclean_size', 
                   'autoclean_days', 'autoclean_same_count']
