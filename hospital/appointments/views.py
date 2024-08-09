from django.views import generic

from appointments.models import Doctor, Appointment


class OurDoctorsView(generic.ListView):
    model = Doctor
    template_name = 'appointments/our_doctors.html'
    context_object_name = 'doctors'


class DoctorDetailView(generic.DetailView):
    model = Doctor
    template_name = 'appointments/doctor_detail.html'
    context_object_name = 'doctor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['appointments'] = Appointment.objects.filter(doctor_id=self.kwargs.get('pk'))

        return context
