from django.http import HttpResponse
from django.shortcuts import render
from myrm_app.view_classes.bukkit_list import BukkitList
from myrm_app.view_classes.bukkit_add import BukkitAdd
from myrm_app.view_classes.bukkit_details import BucketDetails
from myrm_app.view_classes.bukkit_edit import BucketEdit
from myrm_app.view_classes.bucket_remove import bucket_remove
from myrm_app.view_classes.task_list import TaskList
from myrm_app.view_classes.task_add import TaskAdd
from myrm_app.view_classes.task_details import TaskDetails
from myrm_app.view_classes.task_edit import TaskEdit
from myrm_app.view_classes.task_remove import task_remove
# Create your views here.

def say_hellow(request):
    return HttpResponse("Hellow")
