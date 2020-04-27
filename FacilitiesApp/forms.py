from django import forms
from django.forms import ModelForm

from .models import Ticket


YEAR_CHOICES = ['2019', '2020', '2021', '2022', '2023', '2024']

REPAIR_CHOICES = (
    ('New', 'New'),
    ('Received', 'Received'),
    ('Waiting sparts', 'Waiting sparts'),
    ('Waiting contactor', 'Waiting contactor'),
    ('Repair done', 'Repair done')
    )

REPAIR_Y_CHOICES = (
    ('None', 'This year'),
    ('2020', '2020'),
    ('2021', '2021'),
    ('2022', '2022'),
    ('2023', '2023'),
    ('2024', '2024')
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

    

        