from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .models import Worker

# TODO remove function later
import random
import socket
import struct
def get_random_ip():
    return socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))

@require_http_methods(["GET", "POST"])
def get_browser_box(request):
    if  request.method == 'POST':
        worker = Worker.objects.order_by('?')[0]
        url = f'https://{worker.ip!s}:8080'
        context = {'browserbox_url': url}
        return render(request, 'browserbox/success.html', context)
    else:
        return render(request, 'browserbox/request.html')
