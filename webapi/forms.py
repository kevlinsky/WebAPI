from django import forms
from django.forms import SelectDateWidget, SplitDateTimeWidget
from .models import *


class TicketForm(forms.ModelForm):
    date = forms.DateField(widget=SelectDateWidget(years=[y for y in range(2000, 2020)]))
    time = forms.TimeField(label='Time (HH:MM:SS):')

    class Meta:
        model = Ticket
        fields = (
            'number',
            'date',
            'time',
        )
