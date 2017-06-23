from django.http import HttpResponse
from django.shortcuts import render
from myrm_app.view_classes.bucket_list import BucketList
from myrm_app.view_classes.bucket_add import BucketAdd
from myrm_app.view_classes.bucket_details import BucketDetails
from myrm_app.view_classes.bucket_edit import BucketEdit
from myrm_app.view_classes.bucket_remove import bucket_remove
from myrm_app.view_classes.task_list import TaskList
from myrm_app.view_classes.task_add import TaskAdd
from myrm_app.view_classes.task_details import TaskDetails
from myrm_app.view_classes.task_edit import TaskEdit
from myrm_app.view_classes.task_remove import task_remove
from myrm_app.view_classes.disk import Disk

def say_hellow(request):
    return HttpResponse("Hellow")
