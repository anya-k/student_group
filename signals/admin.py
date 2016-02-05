from django.contrib import admin
from models import Signal


class SignalAdmin(admin.ModelAdmin):
    list_display = ('date_time', 'name_model', 'event', 'name_object')
    # ordering = 'date_time'

admin.site.register(Signal, SignalAdmin)