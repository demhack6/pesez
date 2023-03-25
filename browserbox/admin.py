from django.contrib import admin
from .models import BrowserBox, HistoryBrowserBox, Worker


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('id', 'ip', 'available')
    search_fields = ('id', 'ip', 'available')


@admin.register(BrowserBox)
class BrowserBoxAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('id', 'ip')
    search_fields = ('id', 'ip')


@admin.register(HistoryBrowserBox)
class BrowserBoxSessionAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('id', 'ip')
    search_fields = ('id', 'ip')
