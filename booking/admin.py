from django.contrib import admin
from . models import *
# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
  list_display = ['user','room','display','room_num','booking_code','checkin','checkout','no_days','amount','paid','available','booking_date','checkout_update','future']
  readonly_fields = ['user','room','room_num','booking_code','checkin','checkout','no_days','amount','paid']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user','first_name','last_name','amount','paid','phone','pay_code','payment_date','admin_upadate','admin_note'] #check where to add future
    readonly_fields = ['user','first_name','last_name','amount','paid','phone','pay_code']  # this makes this fields to be read only so that only admin can edit the field