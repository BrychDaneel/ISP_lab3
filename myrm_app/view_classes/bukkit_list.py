from django.views.generic import ListView
from myrm_app.models import Bukkit

class BukkitList(ListView):
    template_name = "bukkit_list.html"
    model = Bukkit
