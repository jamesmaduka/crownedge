from django import Forms
from django.forms import ModelForm
from . models import *


class BookingForm(Forms.ModelForm):
    class Meta:
      model = Booking
      fields = ['checkin','checkout']