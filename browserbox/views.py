from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .models import BrowserBox

# TODO remove function later
import random
import socket
import struct
def get_random_ip():
    return socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))

@require_http_methods(["GET", "POST"])
def get_browser_box(request):
    if  request.method == 'POST':
        bb = BrowserBox(ip=get_random_ip())
        bb.save()
        url = f'https://{bb.ip!s}'
        return render(request, 'browserbox/success.html', {'browserbox_url': url})
    else:
        return render(request, 'browserbox/request.html')
