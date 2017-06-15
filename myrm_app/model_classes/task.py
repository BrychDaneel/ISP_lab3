import myrm.remover
import myrm_app.model_classes as myrm_models
from django.db import models
from myrm_app.model_classes.parametrs import Parametrs
from myrm_app.model_classes.bukkit import Bukkit

class Task(models.Model):
    """
    """

    parametrs = models.OneToOneField(Parametrs)
    bukkit = models.ForeignKey(Bukkit, on_delete=models.PROTECT)
    target = models.CharField(max_length=100)
    created = models.TimeField(auto_now=True)
    
    WAITING = "waiting"
    CANCELED = "canceled"
    RUNNING = "running"
    COMPLETED = "completed"
    STATUS_CHOISCES = (
        (COMPLETED, "Waitint"),
        (CANCELED, "Canceled"),
        (RUNNING, "Running"),
        (COMPLETED, "Completed"),
    )
    status = models.CharField(choices=STATUS_CHOISCES, default=WAITING, max_length=30)

    REMOVE = "rm"
    RESTORE = "rs"
    CLEAN = "cl"
    COMMAND_CHOISCES = (
        (REMOVE, "Remove"),
        (RESTORE, "Restore"),
        (CLEAN, "Clean")
    )
    command = models.CharField(choices=COMMAND_CHOISCES, max_length=30)
