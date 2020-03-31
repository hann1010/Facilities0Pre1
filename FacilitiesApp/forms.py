from django import forms
from django.forms import ModelForm

from .models import Ticket

class DateInput(forms.DateInput):
    input_type = 'date'
    
class State_select(forms.NullBooleanSelect):
    input_type = 'text'


class TicketForm(ModelForm):

    class Meta:
        model = Ticket
        fields = ['first_name', 'last_name', 'address', 'received', 'title', 'fault','repair_state','repair', 'date_repair', 'phone_no', 'email', 'house_company', 'notes']
        widgets = {
            'date_repair': DateInput(),
            'repair_state': State_select(),
            'received': State_select(),           
        }

    

        