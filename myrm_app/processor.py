""" Perfom task from database.

Methods:
 * start_process - entry poin
 * 
"""


import threading
import time
from myrm_app.models import Task 
from myrm.remover import Remover
import os


def _process():
        while True:
            query_set = Task.objects.filter(status=Task.WAITING)
            
            if not query_set.exists(): 
                time.sleep(1)
                continue

            task = query_set.latest('created')

            params = task.parametrs.struct()
            bucket_path = os.path.join('buckets', task.bucket.directory)
            params['trash']['directory'] = bucket_path
            remover = Remover(**params)
            target = os.path.join('disk', task.target)
            task.status = Task.RUNNING
            task.save()
            try:
                if task.command == Task.REMOVE:
                    remover.remove(target)

                elif task.command == Task.RESTORE:
                    remover.restore(target)

                elif task.command == Task.CLEAN:
                    remover.clean(target)

            except Exception as error:
                task.status = Task.ERROR
                task.save()
            else:
                task.status = Task.COMPLETED
                task.save()


def start_process(first_run=[]):
    """Starts endless cyrcle.
    """
    if first_run:
        return
    first_run.append(True)
    thread = threading.Thread(target=_process)
    thread.setDaemon(True)
    thread.start()
