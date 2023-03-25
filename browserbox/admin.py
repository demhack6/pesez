from django.contrib import admin
from .models import BrowserBox, Worker


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('id', 'ip', 'status')
    search_fields = ('id', 'ip', 'status')


@admin.register(BrowserBox)
class BrowserBoxAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('id', 'ip')
    search_fields = ('id', 'ip')
