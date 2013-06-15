from django.contrib import admin
from main.models import Appointment, Problem

class AppointmentAdmin(admin.ModelAdmin):
    pass

class ProblemAdmin(admin.ModelAdmin):
    pass

admin.site.register(Problem, ProblemAdmin)
admin.site.register(Appointment, AppointmentAdmin)
