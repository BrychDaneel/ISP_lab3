from django.conf.urls import url
from myrm_app.view_classes.bukkit_list import BukkitList
import myrm_app.views as views

urlpatterns = [
    url(r'^$', views.say_hellow, name='say_hellow'),
    url(r'^bukkits$', BukkitList.as_view(), name='bukkit_list')
]
