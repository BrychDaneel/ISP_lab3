"""Contains Bucket model.

Classes:
 * Bucket
"""


import myrm.trash
import myrm.autocleaner
from django.db import models
from django.core.validators import RegexValidator
from myrm_app.model_classes.parametrs import Parametrs


class Bucket(models.Model):
    """Store bucket parametrs.
    """

    name = models.CharField(unique=True, max_length=30)
    directory = models.CharField(unique=True, max_length=30,
                                 validators=[RegexValidator(r"^\w+$")])
    parametrs = models.OneToOneField(Parametrs, on_delete=models.CASCADE)
    locked = models.BooleanField(default=False)
        
    def __unicode__(self):
        return self.name
