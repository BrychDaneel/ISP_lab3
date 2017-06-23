from django.contrib import admin
from myrm_app.models import Parametrs
from myrm_app.models import Bucket
from myrm_app.models import Task


# Register your models here.
admin.site.register(Parametrs)
admin.site.register(Bucket)
admin.site.register(Task)
