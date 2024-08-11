from django import forms

from appointments.models import Feedback


class AddFeedbackForm(forms.ModelForm):
    text = forms.CharField(max_length=500, widget=forms.TextInput(attrs={
        'placeholder': 'Текст відгука',
    }))

    class Meta:
        model = Feedback
        fields = ['text']