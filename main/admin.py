from django.contrib import admin
from main.models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Appointment, AppointmentAdmin)
