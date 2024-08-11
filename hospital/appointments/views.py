from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import HttpResponseRedirect

from appointments.models import Doctor, Appointment, Feedback
from appointments.forms import AddFeedbackForm


class OurDoctorsView(generic.ListView):
    model = Doctor
    template_name = 'appointments/our_doctors.html'
    context_object_name = 'doctors'


class DoctorDetailView(generic.DetailView, generic.FormView):
    model = Doctor
    template_name = 'appointments/doctor_detail.html'
    context_object_name = 'doctor'
    form_class = AddFeedbackForm
    success_url = reverse_lazy('hms_site:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['appointments'] = Appointment.objects.filter(doctor_id=self.kwargs.get('pk'))
        context['feedbacks'] = Feedback.objects.filter(doctor_id=self.kwargs.get('pk'))

        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.doctor = Doctor.objects.get(id=self.kwargs.get('pk'))
        form.save()
        return HttpResponseRedirect(reverse_lazy('appointments:our_doctors'))


class FeedbackUpdateView(generic.UpdateView):
    model = Feedback
    fields = ['text']
    template_name = 'appointments/feedback-update.html'
    success_url = reverse_lazy('appointments:our_doctors')


class FeedbackDeleteView(generic.DeleteView):
    model = Feedback
    success_url = reverse_lazy('appointments:our_doctors')
    template_name = 'appointments/feedback_delete.html'