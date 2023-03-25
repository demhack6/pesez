from django.urls import path

from . import views

urlpatterns = [
    path('get_browser/', views.get_browser_box, name='browser'),
]