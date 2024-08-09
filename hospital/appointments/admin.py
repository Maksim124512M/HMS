from django.contrib import admin

from appointments.models import Doctor, Appointment


admin.site.register(Doctor)
admin.site.register(Appointment)
