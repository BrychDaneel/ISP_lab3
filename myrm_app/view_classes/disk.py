import os
from django.views.generic import TemplateView
from django.http import Http404
from myrm_app.models import Bukkit
from myrm_app.view_classes.disk_item import DiskItem
from myrm.remover import Remover
from django.shortcuts import get_object_or_404
from myrm.stamp import get_file_list_dict

class Disk(TemplateView):

    template_name = "disk.html"
    base_path = 'disk'
    path = base_path
    bucket = None

    def get(self, request, *args, **kwargs):
        if 'bucket' in request.GET:
            self.bucket = get_object_or_404(Bukkit, pk=request.GET['bucket'])
        if 'dir' in request.GET:
            new_path = os.path.join(self.path, request.GET['dir'])
            if not os.path.exists(new_path) and not self.bucket:
                raise Http404("Directory does not exist")
            self.path = new_path
        return super(Disk, self).get(request, *args, **kwargs)
    
    def get_items_list(self):
        real_items = []
        if os.path.exists(self.path):
            real_items = os.listdir(self.path)
        real_files = []
        real_dirs = []
        bucket_files = []
        bucket_dirs = []
        for item_name in real_items:
            item_path = os.path.join(self.path, item_name)
            rel_path = os.path.relpath(item_path, self.base_path)
            is_dir = os.path.isdir(item_path)
            item = DiskItem(item_name, is_dir=is_dir, path=rel_path)
            if is_dir:
                real_dirs.append(item)
            else:
                real_files.append(item)

        if self.bucket:
            bucket_path = os.path.join('buckets', self.bucket.directory)
            params = {'trash': {'directory': bucket_path}}
            remover = Remover(**params)
            bucket_items = remover.lst(os.path.join(self.path,'*'), 
                                       recursive=False, versions=True)
            files_versions = get_file_list_dict(bucket_items)
            for file_path in files_versions:
                for version in files_versions[file_path]:
                    file_name = os.path.basename(file_path)
                    item_path = os.path.join(self.path, file_name)
                    rel_path = os.path.relpath(item_path, self.base_path)
                    if not version:
                        item = DiskItem(file_name, is_removed=True, 
                                        is_dir=True, path=rel_path)
                        bucket_dirs.append(item)
                    else:
                        item = DiskItem(file_name, is_removed=True, 
                                        is_dir=False, path=rel_path)
                        bucket_files.append(item)
        disk_items = real_dirs + bucket_dirs + real_files + bucket_files
        return disk_items
    
    def get_context_data(self, **kwargs):
        context = super(Disk, self).get_context_data(**kwargs)
        context['disk_items'] = self.get_items_list()
        if os.path.exists(self.path) and os.path.samefile(self.base_path, self.path):
            up = ''
        else:
            dr = os.path.split(self.path)[0]
            up = os.path.relpath(dr, self.base_path)
        context['up'] = up
        context['bucket'] = self.bucket
        return context
