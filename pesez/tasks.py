import datetime
from itertools import islice

from browserbox.models import BrowserBox
from .celery import app


@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

@app.task
def clean_old_boxes():
    now = datetime.datetime.now()
    BrowserBox.objects.filter(terminate_dt__lte=now).update(archived=True)

