import threading
import time
from myrm_app.models import 

def start_process(first_run=[]):
    if first_run:
        return
    first_run.append(True)
    thread = threading.Thread(target=process)
    thread.setDaemon(True)
    thread.start()


def process():
        while True:
            Task
            time.sleap(1000)
