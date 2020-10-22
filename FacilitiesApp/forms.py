from django import forms
from django.forms import ModelForm
import datetime
from .models import Ticket
from functools import partial


date_year = int(datetime.datetime.now().strftime('%Y'))


#YEAR_CHOICES = [date_year-1, date_year, date_year+1]

REPAIR_CHOICES = (
    ('New', 'New'),
    ('Received', 'Received'),
    ('Waiting sparts', 'Waiting sparts'),
    ('Work in progress', 'Work in progress'),
    ('Repair done', 'Repair done')
    )

REPAIR_Y_CHOICES = (
    ('None', 'All'),
    (date_year, date_year),
    (date_year-1, date_year-1),
    (date_year-2, date_year-2),
    (date_year-3, date_year-3),
    (date_year-4, date_year-4),
    (date_year-5, date_year-5)
    )

class FilterForm(forms.Form):
    filter_repair_state = forms.ChoiceField(choices = REPAIR_CHOICES)
    posted_year = forms.ChoiceField(choices = REPAIR_Y_CHOICES)

#class DatePicker(forms.DateInput):
#    input_type = 'date'

DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class TicketFormNew(ModelForm):
    class Meta:
        model = Ticket
        fields = ['first_name', 'last_name', 'address', 'title', 'fault', 'phone_no', 'email', 'house_company', 'notes']
        widgets = {
            
                      
        }

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['first_name', 'last_name', 'address', 'title', 'fault','repair', 'repair_state', 'date_repair', 'phone_no', 'email', 'house_company', 'notes']
        widgets = {
            'date_repair': DateInput(),
            'repair_state': forms.Select(choices = REPAIR_CHOICES),
                      
        }

    

        