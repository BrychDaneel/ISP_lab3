import myrm.remover
import myrm_app.model_classes as myrm_models
from django.db import models
from myrm_app.model_classes.parametrs import Parametrs
from myrm_app.model_classes.bukkit import Bukkit

class Task(models.Model):
    """
    """

    bukkit = models.ForeignKey(Bukkit, on_delete=models.PROTECT)
    parametrs = models.OneToOneField(Parametrs)
    target = models.CharField(max_length=100)
    created = models.TimeField(auto_now=True)
    
    WAITING = "waiting"
    CANCELED = "canceled"
    RUNNING = "running"
    COMPLETED = "completed"
    
    STATUS_CHOISCES = (
        (COMPLETED, "Completed"),
        (CANCELED, "Canceled"),
        (RUNNING, "Running"),
        (COMPLETED, "Completed"),
    )
    
    status = models.TextField(choices=STATUS_CHOISCES, default=WAITING)
