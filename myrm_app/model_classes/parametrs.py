import myrm.remover
import myrm.trash
import myrm.autocleaner
from django.db import models


class Parametrs(models.Model):
    
    force = models.BooleanField(default=myrm.remover.DEFAULT_FORCE)
    dryrun = models.BooleanField(default=myrm.remover.DEFAULT_DRYRUN)
    auto_replace = models.BooleanField(default=myrm.remover.DEFAULT_AUTO_REPLACE)
    allow_autoclean = models.BooleanField(default=myrm.remover.DEFAULT_ALLOW_AUTOCLEAN)

    trash_max_size = models.BigIntegerField(default=myrm.trash.DEFAULT_MAX_SIZE)
    trash_max_count = models.BigIntegerField(default=myrm.trash.DEFAULT_MAX_COUNT)

    autoclean_count = models.BigIntegerField(default=myrm.autocleaner.DEFAULT_CLEAN_COUNT)
    autoclean_size = models.BigIntegerField(default=myrm.autocleaner.DEFAULT_CLEAN_SIZE)
    autoclean_days = models.BigIntegerField(default=myrm.autocleaner.DEFAULT_CLEAN_DAYS)
    autoclean_same_count = models.BigIntegerField(default=myrm.autocleaner.DEFAULT_CLEAN_SAME_COUNT)
