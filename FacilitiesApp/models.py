from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Apartment(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True)
    phone_no = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100)
    house_company = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.address + " " + self.last_name

def get_absolute_url(self):
        return reverse('apartment-detail', kwargs={'pk': self.pk})
