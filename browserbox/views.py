from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from .models import BrowserBox

# TODO remove function later
import random
import socket
import struct
def get_random_ip():
    return socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))


def get_browser_box(request):
    if request.user.is_authenticated:
        bb = BrowserBox(ip=get_random_ip())
        bb.save()
        return render(request, f'browsers/{bb.id}', {'browserbox': bb})
    else:
        raise PermissionDenied
