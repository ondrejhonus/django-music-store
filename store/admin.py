from django.contrib import admin

# Register your models here.

from .models import Instrument, InstrumentCategory, InstrumentType

admin.site.register(Instrument)
admin.site.register(InstrumentCategory)
admin.site.register(InstrumentType)