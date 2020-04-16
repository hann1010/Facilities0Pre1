from django import forms
from django.forms import ModelForm

from .models import Ticket


YEAR_CHOICES = ['2019', '2020', '2021', '2022', '2023', '2024']

CHOICES = (
            (0, "New"),
            (1, "Received"),
            (2, "Waiting someting"),
            (3, "Repair done")
           )

class State_select(forms.NullBooleanSelect):
    input_type = 'text'


class TicketForm(ModelForm):

    class Meta:
        model = Ticket
        fields = ['first_name', 'last_name', 'address', 'received', 'title', 'fault','repair_state','repair', 'date_repair', 'phone_no', 'email', 'house_company', 'notes']
        widgets = {
            'date_repair': forms.SelectDateWidget(years=YEAR_CHOICES),
            'repair_state': forms.Select(choices = CHOICES),
            'received': State_select(),           
        }

    

        