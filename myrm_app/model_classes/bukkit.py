import myrm.trash
import myrm.autocleaner
from django.db import models
from django.core.validators import RegexValidator
from myrm_app.model_classes.parametrs import Parametrs

class Bukkit(models.Model):
    """
    """

    name = models.CharField(unique=True, max_length=30)
    directory = models.CharField(unique=True, max_length=30,
                                 validators=[RegexValidator(r"^\w+$")])
    parametrs = models.OneToOneField(Parametrs, on_delete=models.CASCADE)
    locked = models.BooleanField(default=False)

    def delete(self):
        parametrs = self.parametrs
        super(Bukkit)
        
    def __unicode__(self):
        return self.name
