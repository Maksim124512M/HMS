from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


User = get_user_model()


class Appointment(models.Model):
    patient_name = models.CharField(max_length=80)
    patient_description = models.TextField()
    patient_phone_number = models.CharField(max_length=25)
    appointment_date_and_time = models.DateTimeField()
    doctor = models.ForeignKey('Doctor', on_delete=models.DO_NOTHING, related_name='doctor_appointment')

    def __str__(self):
        return self.patient_name

    class Meta:
        verbose_name = 'Прийом'
        verbose_name_plural = 'Прийоми'
    

class Doctor(User):
    role = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.username} - {self.role}'

    def get_absolute_url(self):
        return reverse('appointments:doctor_detail', kwargs={'pk': self.id})

    class Meta:
        verbose_name = 'Лікар'
        verbose_name_plural = 'Лікарі'