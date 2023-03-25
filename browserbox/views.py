from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render


def get_dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'browserbox/base.html', {'user': request.user})
    else:
        raise PermissionDenied
