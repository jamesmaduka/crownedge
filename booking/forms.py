from django import Forms
from django.forms import ModelForm
from . models import *


class BookingForm(forms.ModelForm):
    class Meta:
      model = Booking
      fields = ['checkin','checkout']