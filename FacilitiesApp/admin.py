from django.contrib import admin
from .models import Apartment
from .models import Ticket

admin.site.register(Apartment)
admin.site.register(Ticket)
