from django.conf.urls import url
from myrm_app.views import BucketList
from myrm_app.views import BucketAdd
from myrm_app.views import BucketDetails
from myrm_app.views import BucketEdit
from myrm_app.views import bucket_remove
from myrm_app.views import TaskList
from myrm_app.views import TaskAdd
from myrm_app.views import TaskDetails
from myrm_app.views import TaskEdit
from myrm_app.views import task_remove
from myrm_app.views import Disk
import myrm_app.views as views

urlpatterns = [
    url(r'^$', views.say_hellow, name='say_hellow'),
    url(r'^buckets$', BucketList.as_view(), name='bucket_list'),
    url(r'^buckets/add$', BucketAdd.as_view(), name='bucket_add'),
    url(r'^buckets/bucket(?P<id>\d+)$', BucketDetails.as_view(), name='bucket_detail'),
    url(r'^buckets/bucket(?P<id>\d+)/edit$', BucketEdit.as_view(), name='bucket_edit'),
    url(r'^buckets/bucket(?P<id>\d+)/remove$', bucket_remove, name='bucket_remove'),
    url(r'^tasks$', TaskList.as_view(), name='task_list'),
    url(r'^tasks/add$', TaskAdd.as_view(), name='task_add'),
    url(r'^tasks/bucket(?P<id>\d+)$', TaskDetails.as_view(), name='task_detail'),
    url(r'^tasks/bucket(?P<id>\d+)/edit$', TaskEdit.as_view(), name='task_edit'),
    url(r'^tasks/bucket(?P<id>\d+)/remove$', task_remove, name='task_remove'),
    url(r'^disk$', Disk.as_view(), name='disk')
]
