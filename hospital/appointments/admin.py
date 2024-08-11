from django.contrib import admin

from appointments.models import Doctor, Appointment, Feedback


admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Feedback)