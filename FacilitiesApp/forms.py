from django import forms
from django.forms import ModelForm
import datetime
from .models import Ticket


date_year = int(datetime.datetime.now().strftime('%Y'))


YEAR_CHOICES = [date_year-1, date_year, date_year+1]

REPAIR_CHOICES = (
    ('New', 'New'),
    ('Received', 'Received'),
    ('Waiting sparts', 'Waiting sparts'),
    ('Waiting contactor', 'Waiting contactor'),
    ('Repair done', 'Repair done')
    )

REPAIR_Y_CHOICES = (
    ('None', date_year),
    (date_year-1, date_year-1),
    (date_year-2, date_year-2),
    (date_year-3, date_year-3),
    (date_year-4, date_year-4),
    (date_year-5, date_year-5)
    )

class FilterForm(forms.Form):
    filter_repair_state = forms.ChoiceField(choices = REPAIR_CHOICES)
    repair_year = forms.ChoiceField(choices = REPAIR_Y_CHOICES)


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['first_name', 'last_name', 'address', 'title', 'fault','repair_state','repair', 'date_repair', 'phone_no', 'email', 'house_company', 'notes']
        widgets = {
            'date_repair': forms.SelectDateWidget(years = YEAR_CHOICES),
            'repair_state': forms.Select(choices = REPAIR_CHOICES),
                      
        }

    

        