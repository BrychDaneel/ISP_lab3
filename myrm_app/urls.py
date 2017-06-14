from django.conf.urls import url
from myrm_app.view_classes.bukkit_list import BukkitList
from myrm_app.view_classes.bukkit_add import BukkitAdd
import myrm_app.views as views

urlpatterns = [
    url(r'^$', views.say_hellow, name='say_hellow'),
    url(r'^bukkits$', BukkitList.as_view(), name='bukkit_list'),
    url(r'^bukkits/add$', BukkitAdd.as_view(), name='add_bukkit')
    url(r'^bukkits/\?id=(?P<id>\d+)$', BukkitDetail.as_view(), name='bukkit_detail')
]
