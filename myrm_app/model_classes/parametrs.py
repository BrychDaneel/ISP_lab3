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
    
    def struct(self):
        params_dict = {}
        params_dict['force'] = self.force
        params_dict['dryrun'] = self.dryrun
        params_dict['auto_replace'] = self.auto_replace
        params_dict['allow_autoclean'] = self.allow_autoclean

        trash_params_dict = {}
        params_dict['trash'] = trash_params_dict
        
        trash_params_dict['max_size'] = self.trash_max_size
        trash_params_dict['max_count'] = self.trash_max_count

        autocl_param_dict = {}
        params_dict['autoclean'] = autocl_param_dict
        
        autocl_param_dict['count'] = self.autoclean_count
        autocl_param_dict['size'] = self.autoclean_size
        autocl_param_dict['days'] = self.autoclean_days
        autocl_param_dict['same_count'] = self.autoclean_same_count
        
        return params_dict
