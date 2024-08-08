from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Appointment(models.Model):
    patient_name = models.CharField(max_length=80)
    patient_description = models.TextField()
    patient_phone_number = models.CharField(max_length=25)
    appointment_date_and_time = models.DateTimeField()

    def __str__(self):
        return self.patient_name

    class Meta:
        verbose_name = 'Прийом'
        verbose_name_plural = 'Прийоми'
    

class Doctor(User):
    doctor_photo = models.ImageField(upload_to='users_images/')
    role = models.CharField(max_length=25)
    appointments = models.ForeignKey(Appointment, on_delete=models.DO_NOTHING, related_name='doctor_appointment')

    def __str__(self):
        return f'{self.username} - {self.role}'

    class Meta:
        verbose_name = 'Лікар'
        verbose_name_plural = 'Лікарі'